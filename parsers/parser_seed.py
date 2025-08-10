from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        time.sleep(2)

        while True:
            time.sleep(2)
            blok_things = self.driver.find_elements(By.CSS_SELECTOR, '.s_ais_hit_products_list.flex.flex-wrap.box-border.overflow-hidden .s_ais_hit.grow-0.shrink-0.flex.justify-center.bg-white')
            # print(blok_things)
            time.sleep(2)
            try:
                for thing in blok_things:
                    self.title_price_decs(thing)
                    print(self.info["title"], "имя товара")
                    print(self.info["price"], "price товара")
                    print(self.info["description"], "description товара")
                    print()
                    if self.info:
                        insert_func(self.info)

            except Exception as e:
                print("Ошибка", e)

            try:
                next_btn = self.driver.find_element(By.CSS_SELECTOR, 'li.ais-Pagination-item.ais-Pagination-item--nextPage a')
                next_page = next_btn.get_attribute("href")
                self.driver.get(next_page)
            except Exception as e:
                print(e, "Достигнут конец страницы")
                break

        self.close_window()
        self.zero_window()

    def sencors1_category(self):
        self.parsing_category("https://www.seeedstudio.com/Module-Open-Source-Sensors-2313.html?bazaar4_retailer-products%5BrefinementList%5D%5Bproduct_category%5D%5B0%5D=Sensor", self.save_bd.check_insert_sensor)
    
    def sencors2_category(self):
        self.parsing_category("https://www.seeedstudio.com/Module-Energy-Monitoring-2316.html?bazaar4_retailer-products%5BrefinementList%5D%5Bproduct_category%5D%5B0%5D=Sensor", self.save_bd.check_insert_sensor)
    
    def sencors3_category(self):
        self.parsing_category("https://www.seeedstudio.com/Module-Room-Sensing-2315.html?bazaar4_retailer-products%5BrefinementList%5D%5Bproduct_category%5D%5B0%5D=Sensor", self.save_bd.check_insert_sensor)
    
    def sencors4_category(self):
        self.parsing_category("https://www.seeedstudio.com/Grove-Sensors-c-1974.html?bazaar4_retailer-products%5BrefinementList%5D%5Bproduct_category%5D%5B0%5D=Sensor", self.save_bd.check_insert_sensor)

    def title(self, thing):
        try:
            title = thing.find_element(By.CSS_SELECTOR, ".s_ais_p_title").text
            return title
        except:
            return None
    
    def price(self, thing):
        try:
            price_back = thing.find_element(By.CSS_SELECTOR, ".s_ais_p_price_now").text
            price = price_back.replace('$', '')
            return price
        except:
            return None
    
    def description(self, thing):
        try:
            description = thing.find_element(By.CSS_SELECTOR, ".s_ais_p_info-box.grow.relative.flex.flex-col .s_ais_p_desc.text-12.line-clamp-2.leading-5.text-zinc-700").text
            # description = desc_elem.get_attribute("innerText").strip() desc_elem
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
        self.sencors1_category()
        self.sencors2_category()
        self.sencors3_category()
        self.sencors4_category()

    def close_site(self):
        return super().close_site()
        
if __name__ == "__main__":
    mekroe = Mikroe()
    mekroe.parsing_site()
    mekroe.close_site()