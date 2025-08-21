# db_init/catalogs/crud_company.py
# Реализация CRUD с использованием ООП и дженериков 🔧

from typing import Type, TypeVar, Generic, Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
import db_init.catalogs.models_catalogs as model


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


# тип судна
class VesselTypeRepository(BaseRepository[model.VesselType]):
    """ Репозиторий для работы с VesselType"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.VesselType, session)

    def get_by_name(self, name: str) -> Optional[model.VesselType]:
        return self.get_by_field('vessel_type_name', name)

    def create_vessel_types(self, name: str, description: Optional[str] = None) -> model.VesselType:
        """
        Создаёт новую запись или обновляет существующую в таблице vessel_type.

        :param name: уникальное имя типа судна
        :param description: описание типа судна
        :return: объект VesselType
        """
        return self.get_or_create('vessel_type_name', name, description=description)


# классификационное общество
class ClassSocietyRepository(BaseRepository[model.ClassSociety]):
    """ Репозиторий для работы с ClassSociety"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.ClassSociety, session)

    def get_by_name(self, name: str) -> Optional[model.ClassSociety]:
        return self.get_by_field('class_society_name', name)

    def create_class_society_name(self, name: str, description: Optional[str] = None) -> model.ClassSociety:
        """
        Создаёт новую запись или обновляет существующую в таблице class_society.

        :param name: уникальное имя классификационного общества
        :param description: описание классификационного общества
        :return: объект ClassSociety
        """
        return self.get_or_create('class_society_name', name, description=description)


# статус проекта
class ProjStatusRepository(BaseRepository[model.ProjStatus]):
    """Репозиторий для работы с ProjStatus"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.ProjStatus, session)

    def get_by_name(self, name: str) -> Optional[model.ProjStatus]:
        return self.get_by_field('proj_status_name', name)

    def create_proj_status(self, name: str, description: Optional[str] = None) -> model.ProjStatus:
        """
        Создаёт новую запись или обновляет существующую в таблице proj_status.

        :param name: уникальное имя статуса проекта
        :param description: описание статуса проекта
        :return: объект ProjStatus
        """
        return self.get_or_create('proj_status_name', name, description=description)


# заказчик
class CustomerRepository(BaseRepository[model.Customer]):
    """Репозиторий для работы с Customer"""

    def __init__(self, session: Session) -> None:
        super().__init__(model.Customer, session)

    def get_by_name(self, name: str) -> Optional[model.Customer]:
        return self.get_by_field('name', name)

    def create_customer(self, name: str, description: Optional[str] = None) -> model.Customer:
        """
        Создаёт новую запись или обновляет существующую в таблице customer.

        :param name: уникальное имя статуса проекта
        :param description: описание статуса проекта
        :return: объект ProjStatus
        """
        return self.get_or_create('proj_status_name', name, description=description)