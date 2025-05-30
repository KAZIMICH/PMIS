# db/session.py
# Настройка и создание SQLAlchemy Session 🎛️

from typing import Generator, Optional
from sqlalchemy.orm import sessionmaker, Session
from db.connection import get_engine
from utils.logger import LoggerManager

# Инициализация логгера для модуля
logger = LoggerManager(__name__).get_logger()

# Создаём фабрику сессий
SessionLocal = sessionmaker(
    bind=get_engine(),
    autocommit=False,
    autoflush=False,
    future=True
)

def get_db() -> Generator[Session, None, None]:
    """
    Генератор сессии SQLAlchemy для использования в бизнес-логике.
    Используется как контекстный менеджер:
    with get_db() as session:
        ...
    """
    db: Optional[Session] = None
    try:
        db = SessionLocal()
        logger.info("📂 New database session opened")
        yield db
        db.commit()
        logger.info("✅ Database session committed")
    except Exception as e:
        if db:
            db.rollback()
            logger.error(f"🔄 Rollback session due to error: {e}")
        raise
    finally:
        if db:
            db.close()
            logger.info("🔒 Database session closed")
