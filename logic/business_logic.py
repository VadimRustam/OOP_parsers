from logic.dal import DataAccessor


class Businesslogic:
    def __init__(self):
        self.dal = DataAccessor()
    
    def check_insert_audio(self, audio: dict):
        title = audio.get('title')
        price = audio.get('price')
        description = audio.get('description')

        print(f"[DEBUG] title: {title}, price: {price}, desc: {description}")

        if title:
            info = self.dal.insert_audio(title, price, description)
        else:
            print('Данных аудио нет')

        return info
    
    def check_insert_component(self, component: dict):
        title = component.get('title')
        price = component.get('price')
        description = component.get('description')
    
        if title:
            info = self.dal.insert_component(title, price, description)
        else:
            print('Данных component нет')
    
        return info

    def check_insert_data_logging_memory(self, datalogging_memore: dict):
        title = datalogging_memore.get('title')
        price = datalogging_memore.get('price')
        description = datalogging_memore.get('description')
    
        if title:
            info = self.dal.insert_data_logging_memory(title, price, description)
        else:
            print('Данных datalogging_memory нет')
    
        return info
    
    def check_insert_development_board(self, development_board: dict):
        title = development_board.get('title')
        price = development_board.get('price')
        description = development_board.get('description')
    
        if title:
            info = self.dal.insert_development_board(title, price, description)
        else:
            print('Данных development_board нет')
    
        return info
    
    def check_insert_display(self, display: dict):
        title = display.get('title')
        price = display.get('price')
        description = display.get('description')
    
        if title:
            info = self.dal.insert_display(title, price, description)
        else:
            print('Данных display нет')
    
        return info
    
    def check_insert_e_textiles_crafting(self, e__textiles_crefting: dict):
        title = e__textiles_crefting.get('title')
        price = e__textiles_crefting.get('price')
        description = e__textiles_crefting.get('description')
    
        if title:
            info = self.dal.insert_e_textiles_crafting(title, price, description)
        else:
            print('Данных e_textiles_crafting нет')
    
        return info
    
    def check_insert_gps_gnss(self, gps___gnss: dict):
        title = gps___gnss.get('title')
        price = gps___gnss.get('price')
        description = gps___gnss.get('description')
    
        if title:
            info = self.dal.insert_gps_gnss(title, price, description)
        else:
            print('Данных gps_gnss нет')
    
        return info
    
    def check_insert_iot_wireless(self, iot_wireles: dict):
        title = iot_wireles.get('title')
        price = iot_wireles.get('price')
        description = iot_wireles.get('description')
    
        if title:
            info = self.dal.insert_iot_wireless(title, price, description)
        else:
            print('Данных iot_wireless нет')
    
        return info
    
    def check_insert_kit(self, kit: dict):
        title = kit.get('title')
        price = kit.get('price')
        description = kit.get('description')
    
        if title:
            info = self.dal.insert_kit(title, price, description)
        else:    
            print('Данных kit нет')
    
        return info
    
    def check_insert_robotic(self, robotic: dict):
        title = robotic.get('title')
        price = robotic.get('price')
        description = robotic.get('description')
    
        if title:
            info = self.dal.insert_robotic(title, price, description)
        else:    
            print('Данных robotic нет')
    
        return info
    
    def check_insert_sensor(self, sencor: dict):
        title = sencor.get('title')
        price = sencor.get('price')
        description = sencor.get('description')
        
        if title:
            info = self.dal.insert_sensor(title, price, description)
        else:    
            print('Данных sensor нет')
    
        return info
    
    def check_insert_tool(self, tool: dict):
        title = tool.get('title')
        price = tool.get('price')
        description = tool.get('description')
    
        if title:
            info = self.dal.insert_tool(title, price, description)
        else:    
            print('Данных tool нет')
    
        return info
