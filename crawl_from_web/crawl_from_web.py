from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys


class crawl_from_web():
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
            elements = self.driver.find_elements_by_css_selector(css_selector)
            titles = [el.text for el in elements]
            self.driver.close()
            return titles
        except Exception as e:
            self.show_exception(e)
