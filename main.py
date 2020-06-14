from crawl_from_web_tinhte.crawl_from_web_tinhte import crawl_from_web_tinhte
from telegram_bot.telegram_bot import telegram_bot
import json

news = []

if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)

    print("I'm fetching config...")
    url = config['tinhte_vn_url']
    css_selector = config['tinhte_vn_css_selector']
    chat_bot_token = config['chat_bot_token']
    print("I'm crawling data from %s" % (url))

    crawl_bot = crawl_from_web_tinhte(url)
    news = crawl_bot.crawl_title(css_selector)

    bot = telegram_bot(news, chat_bot_token)
    bot.send()
