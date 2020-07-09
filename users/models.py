from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?
# Create your models here.
