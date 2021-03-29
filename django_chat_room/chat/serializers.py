from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Chat


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User
        fields = ("id", "username")


class ChatSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    class Meta:
        model = Chat
        fields = ("username", "text", "email", "created_date", "updated_date")


class ChatCreateSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    class Meta:
        model = Chat
        fields = ("username", "text", "email")


class ChatUpdateSerializer(serializers.ModelSerializer):
    """Chat serializer"""

    updated_date = serializers.DateTimeField()

    class Meta:
        model = Chat
        fields = ("username", "text", "email", "updated_date")

