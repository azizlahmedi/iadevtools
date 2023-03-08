# -*- coding: utf-8 -*-
import json
import logging
import os
import re
import subprocess

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.http import HttpResponseBadRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from neoxam.factory_app import models, consts, forms, clients, backends

log = logging.getLogger(__name__)


def handle_home(request):
    return redirect('factory-tasks')


def handle_tasks(request):
    task_list = models.Task.objects.all().select_related('procedure_revision__procedure', 'compiler').order_by(
        '-created_at')
    paginator = Paginator(task_list, consts.PAGINATION)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return render(request, 'factory/tasks.html', {
        'nav': 'tasks',
        'tasks': tasks,
    })


def handle_task(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    return render(request, 'factory/task.html', {
        'task': task,
    })


def handle_batches(request):
    batch_list = models.Batch.objects.all().order_by('-created_at')
    paginator = Paginator(batch_list, consts.PAGINATION)
    page = request.GET.get('page')
    try:
        batches = paginator.page(page)
    except PageNotAnInteger:
        batches = paginator.page(1)
    except EmptyPage:
        batches = paginator.page(paginator.num_pages)
    return render(request, 'factory/batches.html', {
        'nav': 'batches',
        'batches': batches,
    })


def handle_batch(request, pk):
    batch = get_object_or_404(models.Batch, pk=pk)
    tasks = models.Task.objects.filter(procedure_revision__batches=batch).order_by('procedure_revision')
    return render(request, 'factory/batch.html', {
        'batch': batch,
        'tasks': tasks,
    })


def handle_new_batch(request):
    if request.method == 'POST':
        form = forms.BatchForm(request.POST)
        if form.is_valid():
            head_revision = backends.SubversionBackend().get_head_revision()
            with transaction.atomic():
                batch = form.save()
            for procedure_name in form.cleaned_data['procedure_names']:
                procedure_revision = clients.compile(2016, procedure_name, head_revision, head_revision)
                batch.procedure_revisions.add(procedure_revision)
            return redirect('factory-batch', pk=batch.pk)
    else:
        form = forms.BatchForm()
    return render(request, 'factory/new_batch.html', {
        'nav': 'new-batch',
        'form': form,
    })


def handle_batch_retry(request, pk):
    batch = get_object_or_404(models.Batch, pk=pk)
    index = 2
    name = batch.name
    match = re.search(' #(\d+)$', batch.name)
    if match:
        name = name[:match.span()[0]]
        index = int(match.group(1)) + 1
    new_name = name + ' #%d' % index
    new_batch = models.Batch.objects.create(name=new_name)
    head_revision = backends.SubversionBackend().get_head_revision()
    for procedure_revision in batch.procedure_revisions.all():
        new_procedure_revision = clients.compile(procedure_revision.procedure.schema_version, procedure_revision.procedure.name, head_revision, head_revision, force=True)
        new_batch.procedure_revisions.add(new_procedure_revision)
    return redirect('factory-batch', pk=new_batch.pk)


def handle_compile_legacy_tasks(request):
    task_list = models.CompileLegacyTask.objects.all().order_by('-created_at')
    paginator = Paginator(task_list, consts.PAGINATION)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return render(request, 'factory/compile_legacy_tasks.html', {
        'tasks': tasks,
        'nav': 'compile-legacy',
    })


def handle_compile_legacy_task(request, pk):
    task = get_object_or_404(models.CompileLegacyTask, pk=pk)
    return render(request, 'factory/compile_legacy_task.html', {
        'task': task,
    })


@csrf_exempt
@require_POST
def handle_compile_legacy(request):
    form = forms.CompileLegacyForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest(json.dumps(form.errors))
    with transaction.atomic():
        task = form.save()
    command = [
        'nohup',
        'neoxam',
        'compile_legacy',
        '-i', str(task.pk),
        '-s', str(task.schema_version),
        '-n', task.procedure_name,
    ]
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, preexec_fn=os.setpgrp)
    return HttpResponse('OK')
