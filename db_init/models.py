# db_init/models.py
# Определение ORM-моделей и Declarative Base 📦

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Text, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from typing import Optional

Base = declarative_base()  # 📍 Декларативная база для моделей

# --- Ассоциативные таблицы для many-to-many ---
user_departments = Table(
    'user_departments', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('department_id', Integer, ForeignKey('departments.id'), primary_key=True)
)

user_roles = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

# пользователи
class User(Base):
    """
    Пользователи системы.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String(50), nullable=False, unique=True, comment="Логин пользователя")
    password_hash: str = Column(String(255), nullable=False, comment="Хэш пароля")
    email: str = Column(String(100), nullable=False, unique=True, comment="Email пользователя")
    first_name: Optional[str] = Column(String(50), nullable=True, comment="Имя пользователя")
    last_name: Optional[str] = Column(String(50), nullable=True, comment="Фамилия пользователя")
    phone: Optional[str] = Column(String(20), nullable=True, comment="Телефон пользователя")
    is_active: bool = Column(Boolean, nullable=False, default=True, comment="Флаг активности пользователя")
    last_login_at: Optional[DateTime] = Column(DateTime, nullable=True, comment="Время последнего входа")
    created_at: DateTime = Column(DateTime, server_default=func.now(), nullable=False, comment="Дата создания записи")
    date_of_employment: Optional[DateTime] = Column(DateTime, nullable=True, comment="Дата приема на работу")

    departments = relationship(
        "Department",
        secondary=user_departments,
        back_populates="users"
    )
    roles = relationship(
        "Role",
        secondary=user_roles,
        back_populates="users"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

# отделы компании
class Department(Base):
    """
    Отделы компании.
    """
    __tablename__ = 'departments'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    dep_name: str = Column(String(50), nullable=False, unique=True, comment="Название отдела")
    description: Optional[str] = Column(Text, nullable=True, comment="Описание отдела")

    users = relationship(
        "User",
        secondary=user_departments,
        back_populates="departments"
    )

    def __repr__(self) -> str:
        return f"<Department(id={self.id}, dep_name={self.dep_name})>"

# роли компании
class Role(Base):
    """
    Роли пользователей.
    """
    __tablename__ = 'roles'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    role_name: str = Column(String(50), nullable=False, unique=True, comment="Название роли")
    description: Optional[str] = Column(Text, nullable=True, comment="Описание роли")

    users = relationship(
        "User",
        secondary=user_roles,
        back_populates="roles"
    )

    def __repr__(self) -> str:
        return f"<Role(id={self.id}, role_name={self.role_name})>"

# тип проекта
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

# статусы проектов нового и переоборудования
class NewProjStatus(Base):
    """
    Статусы проекта нового судна.
    """
    __tablename__ = 'new_proj_status'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    new_proj_status_name: str = Column(String(100), nullable=False, unique=True, comment="Название статуса проекта нового судна")
    description: str = Column(String(255), nullable=True, comment="Описание статуса проекта нового судна")

    def __repr__(self) -> str:
        return f"<NewProjStatus(id={self.id}, new_proj_status_name={self.new_proj_status_name})>"

class RefitProjStatus(Base):
    """
    Статусы проекта переоборудования.
    """
    __tablename__ = 'refit_proj_status'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    refit_proj_status_name: str = Column(String(100), nullable=False, unique=True, comment="Название статуса проекта переоборудования")
    description: str = Column(String(255), nullable=True, comment="Описание статуса проекта переоборудования")

    def __repr__(self) -> str:
        return f"<RefitProjStatus(id={self.id}, refit_proj_status_name={self.refit_proj_status_name})>"

# жизненный циклы проектов
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

# шаблоны проектов
class ProjTemplates(Base):
    """
    Шаблоны проектов.
    """
    __tablename__ = 'proj_templates'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    part_rules: str = Column(String(255), comment="Часть правил")
    proj_template_name_ru: str = Column(String(255), nullable=False, comment="Название шаблона проекта на русском")
    proj_template_name_en: str = Column(String(255), nullable=True, comment="Название шаблона проекта на английском")
    proj_template_path: str = Column(String(255), nullable=False, comment="Сетевой путь к шаблону")
    proj_template_reviewed_: str = Column(String(255), nullable=True, comment="Подлежит или нет к рассмотрению в Классификационном обществе")
    description: str = Column(String(255), nullable=True, comment="Описание шаблона проекта, ссылка на нормативку")

    def __repr__(self) -> str:
        return f"<ProjTemplates(id={self.id}, proj_template_name_ru={self.proj_template_name_ru})>"

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
