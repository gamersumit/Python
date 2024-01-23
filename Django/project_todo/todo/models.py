from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    status = models.BooleanField(default=False)