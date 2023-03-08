# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from neoxam.webintake import api

urlpatterns = [
    url(r'^api/user/push/$', api.create_update_user),
    url(r'^api/user/get/(?P<user_name>[\w.]+)/$', api.retrieve_delete_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)
