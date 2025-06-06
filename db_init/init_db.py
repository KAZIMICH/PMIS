# db_init/init_db.py
# Скрипт инициализации базы данных проекта через SQLite

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from utils.logger import LoggerManager
from db_init.models import Base  # 📂 Импорт декларативной базы моделей
from db_init.config import DATABASE_URL  # URL подключения к SQLite БД (файл)


class DBInitializer:
    """
    Класс для инициализации SQLite БД проекта:
      - создаёт файл БД, если он не существует
      - создаёт таблицы на основе моделей
    """

    def __init__(
        self,
        db_url: str = DATABASE_URL,
    ) -> None:
        """
        :param db_url: URL подключения к SQLite БД (файл)
        """
        self.logger = LoggerManager(__name__).get_logger()
        self.db_url: str = db_url
        self.logger.info(f"🚀 DBInitializer создано с URL={self.db_url}")
        self.engine: Engine | None = None  # Engine для работы с БД

    def get_engine(self) -> Engine:
        """
        Создаёт и возвращает SQLAlchemy Engine для SQLite.
        """
        if self.engine is None:
            self.engine = create_engine(
                self.db_url,
                connect_args={"check_same_thread": False},
                future=True,
            )
            self.logger.info(f"🔥 Engine создан для SQLite {self.db_url}")
        return self.engine

    def create_tables(self) -> None:
        """
        Создаёт все таблицы, описанные в metadata Base.
        """
        engine = self.get_engine()
        Base.metadata.create_all(engine)
        self.logger.info("📦 Все таблицы созданы успешно")

    def run(self) -> None:
        """
        Основная точка входа: создаёт таблицы в SQLite БД.
        """
        self.logger.info("🏁 Начинаем инициализацию SQLite БД")
        self.create_tables()
        self.logger.info("🎉 Инициализация SQLite БД завершена")


if __name__ == "__main__":
    DBInitializer().run()
