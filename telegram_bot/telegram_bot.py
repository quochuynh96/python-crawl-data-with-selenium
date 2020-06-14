from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import random
import telegram
import sys


class telegram_bot():
    def __init__(self, news, chat_bot_token):
        self.news = news
        self.chat_bot_token = chat_bot_token

    def show_exception(self, e):
        print(e)
        sys.exit()

    def handle_news(self, bot, update):
        try:
            rand_index = random.randrange(0, len(self.news))
            chat_id = update.message.chat_id

            print("Message from ID:%s, replying..." % (chat_id))
            bot.send_message(chat_id=chat_id,
                             text="*%s*" % (
                                 self.news[rand_index].title),
                             parse_mode=telegram.ParseMode.MARKDOWN_V2)

            bot.send_photo(chat_id=chat_id,
                           photo=self.news[rand_index].thumb)

            bot.send_message(chat_id=chat_id,
                             text="_%s_" % (self.news[rand_index].excerpt),
                             parse_mode=telegram.ParseMode.MARKDOWN_V2)

            bot.send_message(chat_id=chat_id,
                             text="[Xem thêm tại đây...](%s)" % (
                                 self.news[rand_index].link),
                             parse_mode=telegram.ParseMode.MARKDOWN_V2)
            print("Reply done, listening...")
        except Exception as e:
            self.show_exception(e)

    def send(self):
        print("Starting chatbot...")
        updater = Updater(self.chat_bot_token)
        dp = updater.dispatcher

        print("Listening...")
        dp.add_handler(CommandHandler('news', self.handle_news))
        updater.start_polling()
        updater.idle()
