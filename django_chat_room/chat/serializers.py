import re

from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Chat
from django.core.validators import validate_email, EmailValidator


def text_validator(text_area):
    """Message validation (regex to check if message is not empty string, and length < 100)"""

    if re.search("^\s*$", text_area) is None:
        raise serializers.ValidationError('String is empty')


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ("id", "username")


class ChatSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    # Email validation (regex to check if that is real email)
    email = serializers.EmailField(validators=[validate_email])
    text = serializers.CharField(validators=[text_validator])

    class Meta:
        model = Chat
        fields = ("username", "text", "email", "created_date", "updated_date")
        # extra_kwargs = {'email': {'validators': [EmailValidator, ]},}


class ChatCreateSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    # Email validation (regex to check if that is real email)
    email = serializers.EmailField(validators=[validate_email])
    text = serializers.CharField(validators=[text_validator])

    class Meta:
        model = Chat
        fields = ("username", "text", "email")


class ChatUpdateSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    # Email validation (regex to check if that is real email)
    email = serializers.EmailField(validators=[validate_email])
    text = serializers.CharField(validators=[text_validator])
    updated_date = serializers.DateTimeField()

    class Meta:
        model = Chat
        fields = ("username", "text", "email", "updated_date")
