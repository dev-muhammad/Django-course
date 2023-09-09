#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types

from django.conf import settings
from .bot_utils import create_or_update_user

API_TOKEN = settings.TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text.startswith('/start '):
        arguments = message.text[len('/start '):]
        print(f"Received arguments: {arguments}")
    response = "Welcome to bot"
    created = create_or_update_user(message.from_user)
    if created:
        response += "\\n New user"
    else:
        response += "\\n You already were registred!"
    bot.reply_to(message, response)

# Define the custom keyboard markup
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Option 1")
button2 = types.KeyboardButton("Option 2")
button3 = types.KeyboardButton("Option 3")
menu_keyboard.add(button1, button2, button3)

# Define a message handler function for the /menu command
@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot.send_message(message.chat.id, "Here's the menu:", reply_markup=menu_keyboard)

# Define the inline keyboard markup
inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
button11 = types.InlineKeyboardButton("Option 1", callback_data="option1")
button12 = types.InlineKeyboardButton("Option 2", callback_data="option2")
button13 = types.InlineKeyboardButton("Option 3", callback_data="option3")
inline_keyboard.add(button11, button12, button13)

# Define a message handler function for the /inline-menu command
@bot.message_handler(commands=['inline-menu'])
def send_inline_menu(message):
    bot.send_message(message.chat.id, "Here's the inline menu:", reply_markup=inline_keyboard)

# Define a callback query handler function
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "option1":
        bot.send_message(call.message.chat.id, "You selected Option 1.")
    elif call.data == "option2":
        bot.send_message(call.message.chat.id, "You selected Option 2.")
    elif call.data == "option3":
        bot.send_message(call.message.chat.id, "You selected Option 3.")

@bot.message_handler(regexp=r'(?i)\bhello\b')
def echo_message(message):
    bot.reply_to(message, "Hello Human!")

# handler for stickers
@bot.message_handler(content_types=['sticker'])
def handle_sticker_message(message):
    # Get the sticker ID and emoji (if available)
    sticker_id = message.sticker.file_id
    sticker_emoji = message.sticker.emoji if message.sticker.emoji else "No Emoji"

    # Respond to the sticker message
    response_text = f"Received a sticker with ID: {sticker_id}\nEmoji: {sticker_emoji}"
    bot.reply_to(message, response_text)

# Define a message handler function for images
@bot.message_handler(content_types=['photo'])
def handle_image_message(message):
    # Get the file ID of the largest image (last in the list)
    file_id = message.photo[-1].file_id

    # Respond to the image message
    response_text = f"Received an image with file ID: {file_id}"
    bot.reply_to(message, response_text)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Hello")


def run():
    print("Bot is running!")
    bot.infinity_polling(timeout=10, long_polling_timeout = 5)

if __name__ == "__main__":
    run()

