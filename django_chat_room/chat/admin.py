from django.contrib import admin
from chat.models import Chat


class ChatAdmin(admin.ModelAdmin):
    """Chats"""
    list_display = ("username", "text", "created_date", "updated_date")


admin.site.register(Chat, ChatAdmin)
