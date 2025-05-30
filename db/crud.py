# db/crud.py
# Функции CRUD для работы с моделями БД 🔧

from sqlalchemy.orm import Session
from db.models import ProjType, VesselType


def create_proj_types(
    session: Session,
    proj_type_name: str,
    description: str | None = None
) -> ProjType:
    """
    Создаёт новую запись в таблице proj_type.

    Если запись с таким именем уже существует, возвращает её.

    :param session: Экземпляр SQLAlchemy Session
    :param proj_type_name: Уникальное имя типа проекта
    :param description: Описание типа проекта
    :return: Объект ProjType
    """
    # Проверяем, существует ли уже запись с таким именем
    existing = session.query(ProjType).filter(
        ProjType.proj_type_name == proj_type_name
    ).first()
    if existing:
        return existing

    proj_type = ProjType(
        proj_type_name=proj_type_name,
        description=description
    )
    session.add(proj_type)
    session.flush()  # чтобы получить id сразу после вставки
    return proj_type


def get_proj_types(
    session: Session
) -> list[ProjType]:
    """
    Возвращает все записи из таблицы proj_type.

    :param session: Экземпляр SQLAlchemy Session
    :return: Список объектов ProjType
    """
    return session.query(ProjType).order_by(ProjType.id).all()


def create_vessel_types(
    session: Session,
    vessel_type_name: str,
    description: str | None = None
) -> ProjType:
    """
    Создаёт новую запись в таблице proj_type.

    Если запись с таким именем уже существует, возвращает её.

    :param session: Экземпляр SQLAlchemy Session
    :param proj_type_name: Уникальное имя типа проекта
    :param description: Описание типа проекта
    :return: Объект ProjType
    """
    # Проверяем, существует ли уже запись с таким именем
    existing = session.query(VesselType).filter(
        VesselType.vessel_type_name == vessel_type_name
    ).first()
    if existing:
        return existing

    vessel_type = VesselType(
        vessel_type_name=vessel_type_name,
        description=description
    )
    session.add(vessel_type)
    session.flush()  # чтобы получить id сразу после вставки
    return vessel_type

def vessel_proj_types(
    session: Session
) -> list[VesselType]:
    """
    Возвращает все записи из таблицы proj_type.

    :param session: Экземпляр SQLAlchemy Session
    :return: Список объектов ProjType
    """
    return session.query(VesselType).order_by(VesselType.id).all()
