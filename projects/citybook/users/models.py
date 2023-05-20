from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

