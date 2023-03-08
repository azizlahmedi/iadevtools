# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.versioning import views

urlpatterns = [
    url(r'^api/v1/compilation-head/(?P<schema_version>[0-9]+)/$', views.handle_compilation_head),
]
