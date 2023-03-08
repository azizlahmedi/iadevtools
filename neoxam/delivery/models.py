# -*- coding: utf-8 -*-
from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    gp3_url = models.URLField()

    def __str__(self):
        return self.name
