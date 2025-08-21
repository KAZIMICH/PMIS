# db_init/company/models.py
# Определение ORM-моделей и Declarative Base 📦

from db_init.base import Base
from sqlalchemy import Table, Column, Integer, String, Text, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from typing import Optional


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

