# db_init/config.py
# 📦 Статические настройки проекта

# URL подключения к SQLite БД (файл)
DATABASE_URL: str = "sqlite:///./adomat_db.sqlite3?timeout=30"
# Логирование SQL-запросов (для SQLAlchemy echo)
ECHO_SQL: bool = False
