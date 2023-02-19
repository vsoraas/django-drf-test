
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, datetime


class HelloWorld(models.Model):
    id            = models.AutoField(primary_key=True)
    print         = models.CharField(max_length=255, default="Hello world!")
    extra         = models.CharField(max_length=255, default="", null=True)
    sender        = models.CharField(max_length=255, blank=True, null=True)
    from_api      = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)