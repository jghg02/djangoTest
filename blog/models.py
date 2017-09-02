# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=100)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        
