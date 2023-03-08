# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.commons import views

urlpatterns = [
    url(r'^$', views.handle_home, name='commons-home'),
]
