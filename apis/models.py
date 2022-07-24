from django.db import models
from backend.models import *
from django.contrib.auth.models import User
import string
import random

# Create your models here.

class CalendarToken(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=300, null=True)
    client_secret = models.CharField(max_length=300, null=True)
    access_token = models.CharField(max_length=300, null=True)
    refresh_token = models.CharField(max_length=300, null=True)
    token_uri = models.CharField(max_length=300, null=True)
    expiry = models.DateTimeField()

    def __str__(self):
        return self.profile.user.username
    