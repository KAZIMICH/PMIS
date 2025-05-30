# db/models.py
# Определение ORM-моделей и Declarative Base 📦

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func
from typing import Any

Base = declarative_base()  # 📍 Декларативная база для моделей


class ProjType(Base):
    """
    Типы проектов.
    """
    __tablename__ = 'proj_types'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    proj_type_name: str = Column(String(100), nullable=False, unique=True, comment="Название типа проекта")
    description: str = Column(String(255), nullable=True, comment="Описание типа проекта")

    def __repr__(self) -> str:
        return f"<ProjType(id={self.id}, proj_type_name={self.proj_type_name})>"


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