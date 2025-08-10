from selenium.webdriver.common.by import By
from parsers.parser_spark_fun import Sparkfun
import time

class Adafruit(Sparkfun):
    def __init__(self):
        super().__init__()
    
    def open_site(self):
        self.driver.get("https://www.mikroe.com")

    def parsing_category(self, url: str, insert_func):
        self.driver.execute_script(f"window.open('{url}')")
        self.next_window()
        
        time.sleep(2)
        blok_things = self.driver.find_elements(By.CSS_SELECTOR, '#productListing .row.product-listing')
        try:
            for thing in blok_things:
                self.title_price_decs(thing)
                if self.info:
                    insert_func(self.info)
        except Exception as e:
            print("Ошибка", e)

        self.close_window()
        self.zero_window()
        self.close_site()
    
    def sencors_category(self):
        self.parsing_category("https://www.adafruit.com/category/35", self.save_bd.check_insert_sensor)

    def title(self, thing):
        try:
            title = thing.find_element(By.CSS_SELECTOR, ".product-listing-text-wrapper a").text
            return title
        except:
            return None
    
    def price(self, thing):
        try:
            price_back = thing.find_element(By.CSS_SELECTOR, ".price span").text
            price = price_back.replace('$', '')
            return price
        except:
            return None
    
    def description(self, thing):
        try:
            description = thing.find_element(By.CSS_SELECTOR, ".product-description").text
            return description
        except:
            return None

    def title_price_decs(self, thing):
        title = self.title(thing)
        description = self.description(thing)
        price = self.price(thing)

        self.info["price"] = price
        self.info["title"] = title
        self.info["description"] = description
    
    def parsing_site(self):
        self.open_site()
        self.sencors_category()

    def close_site(self):
        return super().close_site()

if __name__ == "__main__":
    adafruit = Adafruit()
    adafruit.parsing_site()
    # adafruit.close_site()