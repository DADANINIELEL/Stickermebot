# -*- coding: utf-8 -*-
import redis
import os
from typing import Optional
import telebot
import time
import random

from telebot.types import User

token = os.environ['TELEGRAM_TOKEN']
API_TOKEN = token

polear = False

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hola mi dueño se avergüenza de mi.")

@bot.message_handler(commands=['pole'])
def toca_polear(message):
    global polear
    bot.send_message(message.chat.id, "En sus puestos")
    bot.send_message(message.chat.id, "3")
    time.sleep(1)
    bot.send_message(message.chat.id, "2")
    time.sleep(1)
    bot.send_message(message.chat.id, "1")
    time.sleep(random.random()+0.5)
    bot.send_message(message.chat.id, "GO POLE GO")
    polear=True

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: message.text=='pole' or message.text=="oro")
def echo_message(message):
    global polear
    if polear==True :
        polear = False
        print(message.message_id)
        bot.reply_to(message, 'aquí la pole')




bot.polling()


# import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars


# some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
# r = redis.from_url(os.environ.get("REDIS_URL"))

