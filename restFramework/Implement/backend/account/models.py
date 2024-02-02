from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    username : models.CharField(max_length = 14)
    password = models.CharField(max_length = 128)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)