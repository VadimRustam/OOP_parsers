from db.config import session_db
from db.models import *


class DataAccessor:
    def insert_audio(self, title, price, description):
        print(f"[DAO] Добавляю в БД: {title}, {price}, {description}")
        with session_db() as session:
            session.add(AudioBase(title=title, price=price, description=description))

    def insert_component(self, title, price, description):
        with session_db() as session:
            session.add(ComponentBase(title=title, price=price, description=description))

    def insert_data_logging_memory(self, title, price, description):
        with session_db() as session:
            session.add(DataLoggingMemoryBase(title=title, price=price, description=description))

    def insert_development_board(self, title, price, description):
        with session_db() as session:
            session.add(DevelopmentBoardBase(title=title, price=price, description=description))

    def insert_display(self, title, price, description):
        with session_db() as session:
            session.add(DisplayBase(title=title, price=price, description=description))

    def insert_e_textiles_crafting(self, title, price, description):
        with session_db() as session:
            session.add(ETextilesCraftingBase(title=title, price=price, description=description))

    def insert_gps_gnss(self, title, price, description):
        with session_db() as session:
            session.add(GPSGNSSBase(title=title, price=price, description=description))

    def insert_iot_wireless(self, title, price, description):
        with session_db() as session:
            session.add(IoTWirelesBase(title=title, price=price, description=description))

    def insert_kit(self, title, price, description):
        with session_db() as session:
            session.add(KitBase(title=title, price=price, description=description))

    def insert_robotic(self, title, price, description):
        with session_db() as session:
            session.add(RoboticBase(title=title, price=price, description=description))

    def insert_sensor(self, title, price, description):
        with session_db() as session:
            session.add(SensorBase(title=title, price=price, description=description))

    def insert_tool(self, title, price, description):
        with session_db() as session:
            session.add(ToolBase(title=title, price=price, description=description))