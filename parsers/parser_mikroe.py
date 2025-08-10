from selenium.webdriver.common.by import By
from parsers.parser_spark_fun import Sparkfun
import time


class Mikroe(Sparkfun):
    def __init__(self):
        super().__init__()
    
    def open_site(self):
        self.driver.get("https://www.mikroe.com")
    
    def parsing_category(self, url: str, insert_func):
        self.driver.execute_script(f"window.open('{url}')")
        self.next_window()

        while True:
            blok_things = self.driver.find_elements(By.CSS_SELECTOR, 'div.af_pl_wrapper ul.product_list.grid.row.af-product-list li')

            try:
                for thing in blok_things:
                    self.title_price_decs(thing)
                    print(self.info["title"], "имя товара")
                    print()
                    if self.info:
                        insert_func(self.info)

            except Exception as e:
                print("Ошибка", e)

            try:
                next_page = self.driver.find_element(By.CSS_SELECTOR, 'li#pagination_next_bottom a').get_attribute("href")
                self.driver.get(next_page)
                time.sleep(3)
            except Exception as e:
                print(e, "Достигнут конец страницы")
                break

        self.close_window()
        self.zero_window()

    def development_boards_category(self):
        self.parsing_category("https://www.mikroe.com/development-boards", self.save_bd.check_insert_development_board)
    
    def audio_category(self):
        self.parsing_category("https://www.mikroe.com/click/audio-and-voice", self.save_bd.check_insert_audio)

    def sencors_category(self):
        self.parsing_category("https://www.mikroe.com/click/sensors", self.save_bd.check_insert_sensor)

    def title(self, thing):
        try:
            title = thing.find_element(By.CSS_SELECTOR, "div.center-block a.product-name").text
            return title
        except:
            return None
    
    def price(self, thing):
        try:
            price_back = thing.find_element(By.CSS_SELECTOR, "div.right-block div.me-product-price").text
            price = price_back.replace('$', '')
            return price
        except:
            return None
    
    def description(self, thing):
        try:
            desc_elem = thing.find_element(By.CSS_SELECTOR, "p.product-desc")
            description = desc_elem.get_attribute("innerText").strip()
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
        # print("Audio")
        # self.audio_category()
        # print("development_boards")
        # self.development_boards_category()
        self.sencors_category()

    def close_site(self):
        return super().close_site()
        
if __name__ == "__main__":
    mekroe = Mikroe()
    mekroe.parsing_site()
    mekroe.close_site()