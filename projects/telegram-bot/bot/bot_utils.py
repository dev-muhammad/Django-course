from .models import BotUsers


def create_or_update_user(user_data)->bool:

    user, created = BotUsers.objects.update_or_create(
        id = user_data.id,
        defaults=dict(
            username = user_data.username,
            first_name = user_data.first_name,
            last_name = user_data.last_name,
            language_code = user_data.language_code,
        )
    )
    print(f"create_or_update_user: {user_data.first_name}")
    return created

def send_message_to_user(bot, user_id, message):

    bot.send_message(user_id, message, parse_mode='HTML')
    print("message sent to user")