# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.backport import views

urlpatterns = [
    url(r'^$', views.handle_home, name='backport-home'),
    url(r'^commits/$', views.handle_commits, name='backport-commits'),
    url(r'^commits/(?P<revision>[0-9]+)/$', views.download_patch, name='backport-commit'),
    url(r'^commits/download/(?P<revision>[0-9]+)/$', views.download_patched_file, name='backport-commit-download'),
    url(r'^commits/hide/(?P<revision>[0-9]+)/$', views.hide_commit, name='backport-commit-hide')
]
