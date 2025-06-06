# db_init/models.py
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

class NewLifeCycle(Base):
    """
    Жизненные циклы проекта нового судна.
    """
    __tablename__ = 'new_life_cycle'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    new_life_cycle_name: str = Column(String(100), nullable=False, unique=True, comment="Название жизненного цикла")
    description: str = Column(String(255), nullable=True, comment="Описание жизненного цикла")

    def __repr__(self) -> str:
        return f"<NewLifeCycle(id={self.id}, new_life_cycle_name={self.new_life_cycle_name})>"

class RefitLifeCycle(Base):
    """
    Жизненные циклы проекта переоборудования.
    """
    __tablename__ = 'refit_life_cycle'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    refit_life_cycle_name: str = Column(String(100), nullable=False, unique=True, comment="Название жизненного цикла")
    description: str = Column(String(255), nullable=True, comment="Описание жизненного цикла")

    def __repr__(self) -> str:
        return f"<RefitLifeCycle(id={self.id}, refit_life_cycle_name={self.refit_life_cycle_name})>"

class ProjTemplates(Base):
    """
    Шаблоны проектов.
    """
    __tablename__ = 'proj_templates'

    id: int = Column(Integer, primary_key=True, autoincrement=True)

    part_rules: str = Column(String(255), comment="Часть правил")

    proj_template_name_ru: str = Column(String(255), nullable=False,
                                        comment="Название шаблона проекта на русском")
    proj_template_name_en: str = Column(String(255), nullable=True,
                                        comment="Название шаблона проекта на английском")
    proj_template_path: str = Column(String(255), nullable=False,
                                     comment="Сетевой путь к шаблону")
    proj_template_reviewed_: str = Column(String(255), nullable=True,
                                          comment="Подлежит или нет к рассмотрению в Классификационном обществе")
    description: str = Column(String(255), nullable=True,
                              comment="Описание шаблона проекта, ссылка на нормативку")

    def __repr__(self) -> str:
        return f"<ProjTemplates(id={self.id}, proj_template_name_ru={self.proj_template_name_ru})>"

