# -*- coding: utf-8 -*-
from django.conf.urls import url

from neoxam.eclipse import views

urlpatterns = [
    url(r'^$', views.handle_home, name='eclipse-home'),
    url(r'^compile/$', views.handle_compile, name='eclipse-compile'),
    url(r'^deliver/$', views.handle_deliver, name='eclipse-deliver'),
    url(r'^deliver-test/$', views.handle_new_deliver_test, name='eclipse-new-deliver-test'),
    url(r'^deliver-test/(?P<pk>[0-9]+)/$', views.handle_deliver_test, name='eclipse-deliver-test'),
    url(r'^stats/$', views.handle_stats, name='eclipse-stats'),
    url(r'^runtime/$', views.handle_runtime, name='eclipse-runtime'),
]
