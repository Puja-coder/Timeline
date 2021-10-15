from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

class TimeClock(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(blank=False, max_length=254, verbose_name="clock in")
    clock_out = models.DateTimeField(blank=False, max_length=254, verbose_name="clock out")

