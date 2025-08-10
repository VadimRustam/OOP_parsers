from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from db.config import Base

class AudioBase(Base):
	__tablename__ = "audios"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class ComponentBase(Base):
	__tablename__ = "components"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class DataLoggingMemoryBase(Base):
	__tablename__ = "data_logging_memorys"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class DevelopmentBoardBase(Base):
	__tablename__ = "development_boards"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class DisplayBase(Base):
	__tablename__ = "displays"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class ETextilesCraftingBase(Base):
	__tablename__ = "e_textiles_craftings"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class GPSGNSSBase(Base):
	__tablename__ = "gps_gnsss"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class IoTWirelesBase(Base):
	__tablename__ = "iot_wireless"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class KitBase(Base):
	__tablename__ = "kits"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class RoboticBase(Base):
	__tablename__ = "robotics"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class SensorBase(Base):
	__tablename__ = "sensors"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)

class ToolBase(Base):
	__tablename__ = "tools"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	price: Mapped[float] = mapped_column(nullable=True)
	description: Mapped[str] = mapped_column(nullable=True)