# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.gpatcher import views

urlpatterns = [
    url(r'^$', views.handle_home, name='gpatcher-home'),
    url(r'^patch/$', views.patch_source, name='gpatcher-patch'),
    url(r'^result/$', views.result, name='gpatcher-result'),
]
