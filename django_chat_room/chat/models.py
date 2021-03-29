from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Chat(models.Model):
    """Chat model"""
    username = models.CharField(max_length=150, default="")
    text = models.TextField("Message", max_length=100)
    email = models.EmailField("User email", blank=False, default="")
    created_date = models.DateTimeField("Created date", auto_now_add=True)
    updated_date = models.DateTimeField("Updated date", auto_now_add=True)
