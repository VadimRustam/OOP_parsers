from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from logic.business_logic import Businesslogic
from parsers.parser_spark_fun import Sparkfun
import time

class Dfrobot(Sparkfun):
    def __init__(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.save_bd = Businesslogic()
        self.info = {}

    def open_site(self):
        self.driver.get("https://www.sparkfun.com/all-categories")

    def parsing_category(self, url: str, insert_func):
        self.driver.execute_script(f"window.open('{url}')")
        self.next_window()
        time.sleep(5)
        self.button_global()
        time.sleep(5)
        self.scroll_to_end_page()

        blok_things = self.driver.find_elements(By.CSS_SELECTOR, '.product-item.appearance_3')

        print(len(blok_things))
        try:
            for thing in blok_things:
                window_thing = thing.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                self.driver.execute_script(f"window.open('{window_thing}')")
                time.sleep(2)
                self.next_window()
                self.title_price_decs()
                print(self.info["title"], "имя товара")
                print(self.info["price"], "price товара")
                print(self.info["description"], "description товара")
                print()
                if self.info:
                    insert_func(self.info)
                time.sleep(1)
                self.close_window()
                self.first_window()
        except Exception as e:
            print("Ошибка", e)
        time.sleep(2)
        self.detect_window()

        self.close_window()
        self.zero_window()

    def sencors_category(self):
        self.parsing_category("https://www.dfrobot.com/category-36.html", self.save_bd.check_insert_sensor)

    def title(self):
        try:
            title = self.driver.find_element(By.CSS_SELECTOR, "h1.product-name").text
            return title
        except:
            return None
    
    def price(self):
        try:
            price_back = self.driver.find_element(By.CSS_SELECTOR, ".product-prices.d-flex.align-center").text
            price = price_back.replace('$', '')
            return price
        except:
            return None
    
    def description(self):
        try:
            haed_description = self.driver.find_element(By.CSS_SELECTOR, ".content.Introduction").text
            
            full_description = haed_description.find(".", 300)

            if full_description != -1:
                description = haed_description[:full_description + 1]
                description = description.replace("Introduction", "")
            else:
                description = haed_description[:300]
                description = description.replace("Introduction", "")

            return description
        
        except:
            return None

    def title_price_decs(self):
        title = self.title()
        price = self.price()
        description = self.description()
        
        self.info["title"] = title
        self.info["price"] = price
        self.info["description"] = description

    def scroll_to_end_page(self):
        try:
            prev_count = 0

            while True:
                # Считаем, сколько карточек сейчас на странице
                products = self.driver.find_elements(By.CSS_SELECTOR, ".product-item.appearance_3")
                count = len(products)

                if count == prev_count:
                    print("Достигнут конец страницы")
                    break
                
                prev_count = count

                # Скроллим вниз
                self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
                time.sleep(20)  # ждём подгрузку

        except Exception as e:
            print(e, "Название ошибки при scroll_to_end_page")

    def button_global(self):
        try:
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, "#warehousePop > div > div:nth-child(2) > button").click()
        except Exception as e:
            print(e, "Название ошибки при button_global")


    def parsing_site(self):
        self.open_site()
        self.sencors_category()

if __name__ == "__main__":
    parser = Dfrobot()
    parser.parsing_site()
    parser.close_site()