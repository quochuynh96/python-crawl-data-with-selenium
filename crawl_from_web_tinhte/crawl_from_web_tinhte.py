from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
from time import sleep
from models.news import news


class crawl_from_web_tinhte():
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def show_exception(self, e):
        print(e)
        self.driver.quit()
        sys.exit()

    def crawl_title(self, css_selector):
        try:
            self.driver.get(self.url)

            print("Opening browser...")
            for x in range(0, 1):
                load_more = self.driver.find_elements_by_xpath(
                    "//button[text()='Tải Thêm']")
                load_more[0].click()
                print("Click [Tải Thêm]...")
                sleep(3)

            elements = self.driver.find_elements_by_css_selector(css_selector)
            list_news = []

            print("Fetching data...")
            for el in elements:
                # print(el.get_attribute("href"))
                el_title = el.find_elements_by_css_selector(
                    ".jsx-2418319489 .title")
                # print(el_title[0].text)
                el_excerpt = el.find_elements_by_css_selector(
                    ".jsx-2418319489 .excerpt")
                # print(el_excerpt[0].text)
                el_thumb = el.find_elements_by_css_selector(
                    ".jsx-499497018 .mainImg")
                # print(el_thumb[0].get_attribute("src"))

                list_news.append(
                    news(el_title[0].text, el_excerpt[0].text, el.get_attribute("href"), el_thumb[0].get_attribute("src")))

            print("Done, we have %s news" % (len(list_news)))

            self.driver.close()

            print("Closing browser...")

            return list_news

        except Exception as e:
            self.show_exception(e)
