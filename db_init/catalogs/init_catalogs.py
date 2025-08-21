# db_init/catalogs/init_catalogs.py

from db_init.catalogs.seed_catalogs import (
    seed_vessel_types,
    seed_class_societys,
    seed_proj_status,
)
from db_init.catalogs.models_catalogs import Base
from db_init.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from utils.logger import LoggerManager


class DBInitCatalogs:
    """
    Инициализирует таблицы и запускает наполнение справочников (каталогов).
    """

    def __init__(self, db_url: str = DATABASE_URL) -> None:
        self.logger = LoggerManager(__name__).get_logger()
        self.db_url: str = db_url
        self.engine: Engine | None = None
        self.logger.info(f"🚀 DBInitCatalogs создан с URL={self.db_url}")

    def get_engine(self) -> Engine:
        if self.engine is None:
            self.engine = create_engine(
                self.db_url,
                connect_args={"check_same_thread": False},
                future=True,
            )
            self.logger.info(f"🔌 Engine создан для SQLite: {self.db_url}")
        return self.engine

    def create_tables(self) -> None:
        engine = self.get_engine()
        Base.metadata.create_all(engine)
        self.logger.info("📦 Таблицы каталогов успешно созданы")

    def seed_all(self) -> None:
        seed_vessel_types()
        seed_class_societys()
        seed_proj_status()

    def run(self) -> None:
        self.logger.info("🏁 Запуск инициализации каталогов...")
        self.create_tables()
        self.seed_all()
        self.logger.info("🎉 Каталоги успешно инициализированы")


if __name__ == "__main__":
    DBInitCatalogs().run()
