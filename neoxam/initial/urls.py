# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.initial import views

urlpatterns = [
    url(r'^$', views.handle_home, name='initial-home'),
]
