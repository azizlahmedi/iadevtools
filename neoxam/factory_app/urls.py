# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.factory_app import views

urlpatterns = [
    url(r'^$', views.handle_home, name='factory-home'),
    url(r'^tasks/$', views.handle_tasks, name='factory-tasks'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.handle_task, name='factory-task'),
    url(r'^batches/$', views.handle_batches, name='factory-batches'),
    url(r'^batch/(?P<pk>[0-9]+)/$', views.handle_batch, name='factory-batch'),
    url(r'^new-batch/$', views.handle_new_batch, name='factory-new-batch'),
    url(r'^batch/(?P<pk>[0-9]+)/retry/$', views.handle_batch_retry, name='factory-batch-retry'),
    url(r'^compile-legacy/$', views.handle_compile_legacy, name='factory-compile-legacy'),
    url(r'^compile-legacy-tasks/$', views.handle_compile_legacy_tasks, name='factory-compile-legacy-tasks'),
    url(r'^compile-legacy-task/(?P<pk>[0-9]+)/$', views.handle_compile_legacy_task, name='factory-compile-legacy-task'),
]
