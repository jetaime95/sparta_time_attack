from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    website = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=13, null=True) # -포함 010-xxxx-xxxx