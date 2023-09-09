from django.contrib import admin

from .models import BotUsers
from .bot_utils import send_message_to_user
from .telegram_bot import bot


def send_message(modeladmin, request, queryset):
    
    for user in queryset:
        message = f"Hello {user.first_name}"
        send_message_to_user(bot, user.id, message)
send_message.short_description = "Send message to selected Bot users"

@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "create_datetime"]
    actions = [send_message,]