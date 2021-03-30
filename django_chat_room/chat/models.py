import re

from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError


def text_validator(text_area):
    """Message validation (regex to check if message is not empty string, and length < 100)"""

    if re.search(r"^\s*$", text_area) is not None:
        raise ValidationError('String is empty')


class Chat(models.Model):
    """Chat model"""
    username = models.CharField(max_length=150, default="")
    text = models.TextField("Message", max_length=100, validators=[text_validator])
    email = models.EmailField("User email", blank=False, default="", validators=[EmailValidator])
    created_date = models.DateTimeField("Created date", auto_now_add=True)
    updated_date = models.DateTimeField("Updated date", auto_now_add=True)
