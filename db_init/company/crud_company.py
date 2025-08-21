# db_init/company/crud_company.py
# Реализация CRUD с использованием ООП и дженериков 🔧

from typing import Type, TypeVar, Generic, Optional, List
from sqlalchemy import select, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

import db_init.new_vessel_proj.models as model

# Определяем обобщённый тип модели
ModelType = TypeVar('ModelType', bound=model.Base)


# базовый репозиторий
class BaseRepository(Generic[ModelType]):
    """
    Базовый репозиторий для общих операций CRUD.
    :param model: класс модели SQLAlchemy
    :param session: активная сессия SQLAlchemy
    """
    def __init__(self, model: Type[ModelType], session: Session) -> None:
        self.model = model
        self.session = session

    def get_all(self) -> List[ModelType]:
        """Возвращает все записи из таблицы модели"""
        stmt = select(self.model).order_by(self.model.id)
        result = self.session.scalars(stmt)
        return result.all()

    def get_by_id(self, id_: int) -> Optional[ModelType]:
        """Возвращает запись по первичному ключу или None"""
        return self.session.get(self.model, id_)

    def get_by_field(self, field_name: str, value) -> Optional[ModelType]:
        """Возвращает одну запись по значению указанного поля или None"""
        stmt = select(self.model).filter_by(**{field_name: value})
        try:
            return self.session.scalars(stmt).one()
        except NoResultFound:
            return None

    def create(self, **kwargs) -> ModelType:
        """
        Создаёт и возвращает новую запись.
        """
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.flush()
        return instance

    def update(self, instance: ModelType, **kwargs) -> ModelType:
        """Обновляет поля у переданного экземпляра и возвращает его"""
        for k, v in kwargs.items():
            setattr(instance, k, v)
        self.session.flush()
        return instance

    def delete(self, instance: ModelType) -> None:
        """Удаляет переданный экземпляр из базы"""
        self.session.delete(instance)
        self.session.flush()

    def get_or_create(self, unique_field: str, value, **kwargs) -> ModelType:
        """
        Создаёт или обновляет запись по уникальному полю.
        :param unique_field: имя поля с уникальным ограничением
        :param value: значение уникального поля для поиска
        :param kwargs: дополнительные поля для создания или обновления
        :return: объект модели
        """
        existing = self.get_by_field(unique_field, value)
        if existing:
            # Удаляем из kwargs те ключи, где значение None, чтобы не затирать существующие значения
            update_fields = {k: v for k, v in kwargs.items() if v is not None}
            return self.update(existing, **update_fields)
        return self.create(**{unique_field: value}, **kwargs)


# пользователи с many-to-many
class UserRepository(BaseRepository[model.User]):
    """Репозиторий для работы с User"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.User, session)
        # вспомогательные репозитории
        self.dep_repo = DepartmentRepository(session)
        self.role_repo = RoleRepository(session)

    def get_by_username(self, username: str) -> Optional[model.User]:
        return self.get_by_field('username', username)

    def create_or_update_user(
        self,
        username: str,
        password_hash: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        is_active: bool = True,
        last_login_at: Optional[DateTime] = None,
        created_at: Optional[DateTime] = None,
        date_of_employment: Optional[DateTime] = None,
        departments: Optional[List[str]] = None,
        roles: Optional[List[str]] = None
    ) -> model.User:
        """
        Создаёт новую запись или обновляет существующую в таблице users.

        :param username: уникальный логин
        :param password_hash: хэш пароля
        :param email: электронная почта
        :param first_name: имя
        :param last_name: фамилия
        :param phone: телефон
        :param is_active: флаг активности
        :param last_login_at: время последнего входа
        :param created_at: дата создания
        :param date_of_employment: дата трудоустройства
        :param departments: отделы
        :param roles: роли
        :return: объект model.User
        """
        user = self.get_or_create(
            'username', username,
            password_hash=password_hash,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_active=is_active,
            last_login_at=last_login_at,
            created_at=created_at,
            date_of_employment=date_of_employment
        )
        if departments is not None:
            # создаём/находим и связываем отделы
            user.departments = [self.dep_repo.create_department(name) for name in departments]
        if roles is not None:
            # создаём/находим и связываем роли
            user.roles = [self.role_repo.create_role(name) for name in roles]
        self.session.flush()
        return user


# отделы компании
class DepartmentRepository(BaseRepository[model.Department]):
    """Репозиторий для работы с Department"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.Department, session)

    def get_by_name(self, name: str) -> Optional[model.Department]:
        return self.get_by_field('dep_name', name)

    def create_department(self, name: str, description: Optional[str] = None) -> model.Department:
        """
        Создаёт новую запись или обновляет существующую в таблице departments.

        :param name: уникальное имя отдела
        :param description: описание отдела
        :return: объект Department
        """
        return self.get_or_create('dep_name', name, description=description)


# роли компании
class RoleRepository(BaseRepository[model.Role]):
    """Репозиторий для работы с Role"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.Role, session)

    def get_by_name(self, name: str) -> Optional[model.Role]:
        return self.get_by_field('role_name', name)

    def create_role(self, name: str, description: Optional[str] = None) -> model.Role:
        """
        Создаёт новую запись или обновляет существующую в таблице roles.

        :param name: уникальное имя роли
        :param description: описание роли
        :return: объект Role
        """
        return self.get_or_create('role_name', name, description=description)
