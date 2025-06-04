# db/crud.py
# Реализация CRUD с использованием ООП и дженериков 🔧

from typing import Type, TypeVar, Generic, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from db.models import Base, ProjType, VesselType, ClassSociety, NewLifeCycle, RefitLifeCycle, ProjTemplates

# Определяем обобщённый тип модели
ModelType = TypeVar('ModelType', bound=Base)

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
        return self.session.query(self.model).order_by(self.model.id).all()

    def get_by_field(self, field_name: str, value) -> Optional[ModelType]:
        """Возвращает одну запись по значению указанного поля или None"""
        try:
            query = self.session.query(self.model)
            return query.filter(getattr(self.model, field_name) == value).one()
        except NoResultFound:
            return None

    def create(self, **kwargs) -> ModelType:
        """
        Создаёт и возвращает новую запись.
        Если переданы поля, совпадающие с уникальными, может бросить IntegrityError.
        """
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.flush()  # получить id
        return instance

    def get_or_create(self, unique_field: str, value, **kwargs) -> ModelType:
        """
        Возвращает существующую запись по уникальному полю или создаёт новую.

        :param unique_field: имя поля с уникальным ограничением
        :param value: значение уникального поля для поиска
        :param kwargs: дополнительные поля для создания
        """
        existing = self.get_by_field(unique_field, value)
        if existing:
            return existing
        return self.create(**{unique_field: value}, **kwargs)

class ProjTypeRepository(BaseRepository[ProjType]):
    """Репозиторий для работы с ProjType"""
    def __init__(self, session: Session) -> None:
        super().__init__(ProjType, session)

    def get_by_name(self, name: str) -> Optional[ProjType]:
        return self.get_by_field('proj_type_name', name)

    def create_proj_types(self, name: str, description: Optional[str] = None) -> ProjType:
        return self.get_or_create('proj_type_name', name, description=description)

class VesselTypeRepository(BaseRepository[VesselType]):
    """Репозиторий для работы с VesselType"""
    def __init__(self, session: Session) -> None:
        super().__init__(VesselType, session)

    def get_by_name(self, name: str) -> Optional[VesselType]:
        return self.get_by_field('vessel_type_name', name)

    def create_vessel_types(self, name: str, description: Optional[str] = None) -> VesselType:
        return self.get_or_create('vessel_type_name', name, description=description)

class ClassSocietyRepository(BaseRepository[ClassSociety]):
    """Репозиторий для работы с VesselType"""
    def __init__(self, session: Session) -> None:
        super().__init__(ClassSociety, session)

    def get_by_name(self, name: str) -> Optional[ClassSociety]:
        return self.get_by_field('class_society_name', name)

    def create_class_society_name(self, name: str, description: Optional[str] = None) -> ClassSociety:
        return self.get_or_create('class_society_name', name, description=description)

class NewLifeCycleRepository(BaseRepository[NewLifeCycle]):
    """Репозиторий для работы с NewLifeCycle"""
    def __init__(self, session: Session) -> None:
        super().__init__(NewLifeCycle, session)

    def get_by_name(self, name: str) -> Optional[NewLifeCycle]:
        return self.get_by_field('new_life_cycle_name', name)

    def create_new_life_cycle_name(self, name: str, description: Optional[str] = None) -> NewLifeCycle:
        return self.get_or_create('new_life_cycle_name', name, description=description)

class RefitLifeCycleRepository(BaseRepository[RefitLifeCycle]):
    """Репозиторий для работы с RefitLifeCycle"""
    def __init__(self, session: Session) -> None:
        super().__init__(RefitLifeCycle, session)

    def get_by_name(self, name: str) -> Optional[RefitLifeCycle]:
        return self.get_by_field('refit_life_cycle_name', name)

    def create_refit_life_cycle_name(self, name: str, description: Optional[str] = None) -> RefitLifeCycle:
        return self.get_or_create('refit_life_cycle_name', name, description=description)

class ProjTemplateRepository(BaseRepository[ProjTemplates]):
    """Репозиторий для работы с ProjTemplates"""
    def __init__(self, session: Session) -> None:
        super().__init__(ProjTemplates, session)

    def get_by_name(self, name: str) -> Optional[ProjTemplates]:
        return self.get_by_field('proj_template_name_ru', name)

    def create_proj_template(
            self,
            name_ru: str,
            name_en: Optional[str],
            reviewed: Optional[str],
            path: str,
            description: Optional[str] = None) -> ProjTemplates:
        """Создаёт запись шаблона проекта или возвращает существующую."""
        return self.get_or_create(
            'proj_template_name_ru',
            name_ru,
            proj_template_name_en=name_en,
            proj_template_reviewed_=reviewed,
            proj_template_path=path,
            description=description,
        )

