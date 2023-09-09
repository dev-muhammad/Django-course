from django.contrib import admin
from django.utils import timezone
from .models import Post
from bot.models import BotUsers
from bot.bot_utils import send_message_to_user
from bot.telegram_bot import bot


def send_to_users(modeladmin, request, queryset):
    
    for post in queryset:
        for user in BotUsers.objects.all():
            message = post.get_as_message()
            send_message_to_user(bot, user.id, message)
        post.is_sent = True
        post.send_time = timezone.now()
        post.save()

send_to_users.short_description = "Send post to Bot users"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "is_sent", "send_time"]
    actions = [send_to_users,]