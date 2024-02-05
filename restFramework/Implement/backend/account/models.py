from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=150, blank=False, null = False)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_mode_user = models.BooleanField(default=False)
    is_master_user = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username
    