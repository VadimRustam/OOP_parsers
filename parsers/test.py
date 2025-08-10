from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Настройка опций для Chrome
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Открытие страницы
driver.get("https://www.dfrobot.com/product-1601.html")
time.sleep(3)  # подождать, пока страница загрузится

haed_description = driver.find_element(By.CSS_SELECTOR, ".content.Introduction").text
description = haed_description.find(".", 300)

print(haed_description)



driver.quit()
