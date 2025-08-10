from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from logic.business_logic import Businesslogic
import time


class Sparkfun:
    def __init__(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)
        self.save_bd = Businesslogic()
        self.info = {}

    def open_site(self):
        self.driver.get("https://www.sparkfun.com/all-categories")
    
    """
    parsing_category парсит категории товаров. Сначала открываются все категории (как заглушка). Затем открывается 
    определённая категория, и начинается парсинг: сначала я беру цену, потом открываю страницу товара и парсю остальные данные.
    Когда парсинг категории завершён, вкладка с категорией закрывается, но браузер не закрывается благодаря заглушке open_site. 
    После этого парсятся следующие категории.
    """
    def parsing_category(self, url: str, insert_func):
        self.driver.execute_script(f"window.open('{url}')")
        self.next_window()

        while True:
            blok_things = self.driver.find_elements(By.CSS_SELECTOR, 'ol.products.list.items.product-items li')

            try:
                for thing in blok_things:
                    price = self.price(thing)
                    self.info["price"] = price
                    window_thing = thing.find_element(By.CSS_SELECTOR, '.product-item-info a').get_attribute('href')
                    self.driver.execute_script(f"window.open('{window_thing}')")
                    time.sleep(2)
                    self.next_window()
                    self.title_decs()
                    print(self.info["title"], "имя товара")
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
            
            """Хотел вынести в отельный метод, но нельзя
            использовать break вне цикла
            """
            try:
                self.driver.find_element(By.CSS_SELECTOR, 'li.item.pages-item-next a').click()
                time.sleep(3)
            except Exception as e:
                print(e, "Достигнут конец страницы")
                break

        self.close_window()
        self.zero_window()

    def audio_category(self):
        self.parsing_category("https://www.sparkfun.com/audio.html", self.save_bd.check_insert_audio)

    def components_category(self):
        self.parsing_category("https://www.sparkfun.com/components.html", self.save_bd.check_insert_component)

    def datalogging_memore_category(self):
        self.parsing_category("https://www.sparkfun.com/data-logging-and-memory.html", self.save_bd.check_insert_data_logging_memory)

    def development_boards_category(self):
        self.parsing_category("https://www.sparkfun.com/development-boards.html", self.save_bd.check_insert_development_board)

    def display_category(self):
        self.parsing_category("https://www.sparkfun.com/displays.html", self.save_bd.check_insert_display)

    def e__textiles_crefting_category(self):
        self.parsing_category("https://www.sparkfun.com/e-textiles-crafting.html", self.save_bd.check_insert_e_textiles_crafting)

    def gps___gnss_category(self):
        self.parsing_category("https://www.sparkfun.com/gnss.html", self.save_bd.check_insert_gps_gnss) 

    def iot_wireless_category(self):
        self.parsing_category("https://www.sparkfun.com/iot-wireless.html", self.save_bd.check_insert_iot_wireless)
    
    def kits_category(self):
        self.parsing_category("https://www.sparkfun.com/kits.html", self.save_bd.check_insert_kit)

    def robotics_category(self):
        self.parsing_category("https://www.sparkfun.com/robotics.html", self.save_bd.check_insert_robotic)

    def sencors_category(self):
        self.parsing_category("https://www.sparkfun.com/sensors.html", self.save_bd.check_insert_sensor)

    def tools_category(self):
        self.parsing_category("https://www.sparkfun.com/tools.html", self.save_bd.check_insert_tool)

    """
    detect_window для закрытие рекламы
    """
    def detect_window(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,'[title="Popup CTA"]')))
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='button-container']"))).click()
            self.driver.switch_to.default_content()
            time.sleep(3)
        except:
            self.driver.switch_to.default_content()
            pass

    def title(self):
        try:
            title = self.driver.find_element(By.CSS_SELECTOR, "h1.page-title span.base").text
            return title
        except:
            return None
    
    def price(self, thing):
        try:
            price_back = thing.find_element(By.CSS_SELECTOR, "span.price").text
            price = price_back.replace('$', '')
            return price
        except:
            return None
    
    def description(self):
        try:
            haed_description = self.driver.find_element(By.CSS_SELECTOR, ".product.attribute.description .value").text
            description = haed_description.replace('Product Overview', '').replace('-> <-', '').replace('\n', '')
            return description
        except:
            return None

    def title_decs(self):
        title = self.title()
        description = self.description()
        
        self.info["title"] = title
        self.info["description"] = description
    
    def next_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def zero_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])       
    
    def first_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])       

    def close_window(self):
        self.driver.close()

    def close_site(self):
        self.driver.quit()

    def parsing_site(self):
        self.open_site()
        # self.audio_category() # сдел
        # self.components_category() # сдел
        # self.development_boards_category() # сдел
        # self.datalogging_memore_category()
        # self.display_category()
        # self.e__textiles_crefting_category()
        # self.gps___gnss_category()
        # self.kits_category()
        # self.robotics_category()
        self.sencors_category()
        # self.tools_category()

if __name__ == "__main__":
    parser = Sparkfun()
    parser.parsing_site()
    parser.close_site()