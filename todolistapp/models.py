from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    "Task"
    is_done = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
