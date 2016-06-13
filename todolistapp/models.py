from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    "Task"

    STATES = (
        ('OPEN', 'Open'),
        ('Progress', 'Progress'),
        ('DONE', 'Done'),
        ('CANCELLED', 'Cancelled'),
    )
    is_done = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=STATES, default='OPEN')
