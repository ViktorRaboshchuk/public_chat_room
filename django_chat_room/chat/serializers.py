"""Serializers for converting querysets to JSON"""

from rest_framework import serializers
from chat.models import Chat, text_validator

from django.core.validators import (validate_email)


class ChatSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    class Meta:
        model = Chat
        fields = ("id", "username", "text", "email", "created_date")


class ChatCreateSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    class Meta:
        model = Chat
        fields = '__all__'


class ChatUpdateSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    # Email validation (regex to check if that is real email)
    email = serializers.EmailField(validators=[validate_email])
    text = serializers.CharField(validators=[text_validator])
    updated_date = serializers.DateTimeField()

    class Meta:
        model = Chat
        fields = ("username", "text", "email", "updated_date")
