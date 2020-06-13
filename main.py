from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://dev.to/"
driver.get(url)
time.sleep(3)

elements = driver.find_elements_by_css_selector(".crayons-story__title")
titles = [el.text for el in elements]

print(titles)
