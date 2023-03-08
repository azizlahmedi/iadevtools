# -*- coding: utf-8 -*-
import jsonfield
from django.db import models


class Lock(models.Model):
    name = models.CharField(max_length=64, unique=True)
    data = jsonfield.JSONField()

    def __str__(self):
        return self.name
