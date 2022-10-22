# Python Telegram bot.
#
# 1. Install telebot module: pip3 install pyTelegramBotAPI
# 2. Enter your API Token in the field
# 3. Run!

import telebot

bot = telebot.TeleBot('YOUR API TOKEN HERE')

def launch_bot():
    print('Bot started!')
    bot.infinity_polling()

def get_profile(msg):
    firstname = msg.from_user.first_name
    username = msg.from_user.username or 'none'
    userId = msg.from_user.id
    return 'Name: ' + firstname + '\nUsername: ' + username + '\nUser ID: ' + str(userId)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, 'Hi, send command /profile to get your account information.')

@bot.message_handler(commands=['profile'])
def users_metrics(msg):
    bot.reply_to(msg, get_profile(msg))

launch_bot()