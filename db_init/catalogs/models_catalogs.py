# db_init/catalogs/models.py
# Определение ORM-моделей и Declarative Base 📦

from db_init.base import Base
from sqlalchemy import  Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# тип судна
class VesselType(Base):
    """
    Типы судов.
    """
    __tablename__ = 'vessel_types'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    vessel_type_name: str = Column(String(100), nullable=False, unique=True, comment="Название типа судна")
    description: str = Column(String(255), nullable=True, comment="Описание типа судна")

    def __repr__(self) -> str:
        return f"<VesselType(id={self.id}, vessel_type_name={self.vessel_type_name})>"

# классификационное общество
class ClassSociety(Base):
    """
    Классификационные общества.
    """
    __tablename__ = 'class_societys'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    class_society_name: str = Column(String(100), nullable=False, unique=True, comment="Название классификационного общества")
    description: str = Column(String(255), nullable=True, comment="Описание классификационного общества")

    def __repr__(self) -> str:
        return f"<ClassSociety(id={self.id}, class_society_name={self.class_society_name})>"

# статусы проекта
class ProjStatus(Base):
    """
    Статусы проекта.
    """
    __tablename__ = 'proj_status'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    proj_status_name: str = Column(String(100), nullable=False, unique=True, comment="Название статуса")
    description: str = Column(String(255), nullable=True, comment="Описание статуса")

    def __repr__(self) -> str:
        return f"<ProjStatus(id={self.id}, proj_status_name={self.proj_status_name})>"

# заказчик
class Customer(Base):
    """
    Заказчик.
    """
    __tablename__ = 'customer'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100), nullable=False, unique=True, comment="Полное наименование заказчика")
    short_name: str = Column(String(50), nullable=True, comment="Краткое наименование")
    inn: str = Column(String(12), nullable=True, comment="ИНН")
    kpp: str = Column(String(9), nullable=True, comment="КПП")
    ogrn: str = Column(String(13), nullable=True, comment="ОГРН")
    contact_person: str = Column(String(100), nullable=True, comment="Контактное лицо")
    phone: str = Column(String(20), nullable=True, comment="Телефон")
    email: str = Column(String(100), nullable=True, comment="Email")
    address_legal: str = Column(String(200), nullable=True, comment="Юридический адрес")
    address_actual: str = Column(String(200), nullable=True, comment="Фактический адрес")
    notes: str = Column(Text, nullable=True, comment="Примечания")
    is_active: bool = Column(Boolean, default=True, nullable=False, comment="Запись активна")
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Дата создания")
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False, comment="Дата последнего изменения")

    # связь с проектами (если нужно)
    projects = relationship("ProjectBase", back_populates="customer")

    def __repr__(self) -> str:
        return f"<Customer(id={self.id}, name={self.name})>"


