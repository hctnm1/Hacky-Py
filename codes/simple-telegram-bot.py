# Python Telegram bot.
#
# 1. Install telebot module: pip3 install pyTelegramBotAPI
# 2. Enter your API Token in the field
# 3. Run!

import telebot


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot("YOUR API TOKEN HERE")

    def get_profile(self, msg):
        firstname = msg.from_user.first_name
        username = msg.from_user.username or "none"
        userId = msg.from_user.id
        return (
            "Name: "
            + firstname
            + "\nUsername: "
            + username
            + "\nUser ID: "
            + str(userId)
        )

    def start_handlers(self):
        @self.bot.message_handler(commands=["start"])
        def start(msg):
            self.bot.reply_to(
                msg, "Hi, send command /profile to get your account information."
            )

        @self.bot.message_handler(commands=["profile"])
        def profile(msg):
            self.bot.reply_to(msg, self.get_profile(msg))

    def start_polling(self):
        print("Started polling..")
        return self.bot.infinity_polling()


def launch():
    bot = Bot()
    bot.start_handlers()
    bot.start_polling()


launch()
