# db/connection.py
# Настройка и создание SQLAlchemy Engine 💾

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from utils.logger import LoggerManager
from db.config import DATABASE_URL, ECHO_SQL  # Статические настройки проекта

# Получаем логгер для модуля
logger = LoggerManager(__name__).get_logger()


def get_engine(db_url: str = DATABASE_URL) -> Engine:
    """
    Создаёт и возвращает экземпляр SQLAlchemy Engine.

    :param db_url: URL подключения к БД
    :return: SQLAlchemy Engine
    """
    logger.info(f"🚀 Создаём Engine с URL: {db_url}")
    engine = create_engine(
        db_url,
        echo=ECHO_SQL,
        future=True,
    )
    logger.info("✅ Engine успешно создан")
    return engine
