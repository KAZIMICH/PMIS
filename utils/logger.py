# utils/logger.py
# Центральный менеджер логирования для приложения

import logging
import os
import sys
import textwrap
from logging import Logger
from logging.handlers import RotatingFileHandler
from colorama import init as _colorama_init, Fore, Style

_colorama_init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """
    Форматтер для консоли: INFO — желтый, ERROR — красный. 🌟
    """
    LEVEL_COLORS = {
        logging.INFO: Fore.YELLOW,
        logging.ERROR: Fore.RED,
    }

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        color = self.LEVEL_COLORS.get(record.levelno, "")
        return f"{color}{msg}{Style.RESET_ALL}"


class HtmlFormatter(logging.Formatter):
    """
    Преобразует запись лога в <div> с классом уровня. 📝
    """
    TEMPLATE = (
        '<div class="log {level}">'  
        '[{asctime}] [{levelname}] {message}'
        '</div>\n'
    )

    def __init__(self, datefmt: str | None = None) -> None:
        super().__init__(fmt="%(message)s", datefmt=datefmt)

    def format(self, record: logging.LogRecord) -> str:
        record.message = record.getMessage()
        record.levelname = record.levelname
        record.asctime = self.formatTime(record, self.datefmt)
        level = record.levelname.lower()
        return self.TEMPLATE.format(
            level=level,
            asctime=record.asctime,
            levelname=record.levelname,
            message=record.message
        )


class HtmlFileHandler(RotatingFileHandler):
    """
    Файловый хендлер: выравнивание HEADER через textwrap.dedent. 📄
    """
    HEADER = textwrap.dedent("""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <title>Логи приложения</title>
          <style>
            body { font-family: monospace; background: #f9f9f9; padding: 20px; }
            .log { margin: 2px 0; }
            .error { color: red; }
            .warning { color: orange; }
            .debug { color: gray; }
          </style>
        </head>
        <body>
          <h1>Логи приложения</h1>
        """)
    FOOTER = textwrap.dedent("""
            </body>
            </html>
            """)

    def emit(self, record: logging.LogRecord) -> None:
        # При первом emit() добавляем HEADER ✨
        if self.stream.tell() == 0:
            self.stream.write(self.HEADER)
        msg = self.format(record)
        self.stream.write(msg)
        self.flush()

    def doRollover(self) -> None:
        super().doRollover()
        # При следующем emit() снова добавит HEADER 🔄


class LoggerManager:
    """
    Менеджер логирования для настройки консольного и HTML логирования. 🎛️
    """

    def __init__(self, module_name: str) -> None:
        """
        Инициализация менеджера логирования.
        :param module_name: имя модуля для логгера.
        """
        self.module_name = module_name
        self.logger: Logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:
            self._setup_handlers()

    def get_logger(self) -> Logger:
        """
        Возвращает настроенный экземпляр Logger.
        """
        return self.logger

    def _setup_handlers(self) -> None:
        """Создает и добавляет хендлеры в логгер. 🛠️"""
        console_handler = self._create_console_handler()
        html_handler = self._create_html_handler()
        self.logger.addHandler(console_handler)
        self.logger.addHandler(html_handler)

    def _create_console_handler(self) -> logging.Handler:
        """Создает цветной консольный хендлер. 🌈"""
        fmt = "%(asctime)s - [%(name)s] - %(levelname)s - %(message)s"
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(ColoredFormatter(fmt, datefmt="%H:%M:%S"))
        return handler

    def _create_html_handler(self) -> logging.Handler:
        """Создает HTML файл хендлер. 📄"""
        log_dir = self.get_log_dir()
        html_path = os.path.join(log_dir, "app.html")
        handler = HtmlFileHandler(
            html_path,
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8"
        )
        handler.setLevel(logging.INFO)
        handler.setFormatter(HtmlFormatter(datefmt="%Y-%m-%d %H:%M:%S"))
        return handler

    @staticmethod
    def get_log_dir() -> str:
        """
        Определяет директорию для логов:
          - рядом с .exe при компиляции;
          - иначе — ../logs относительно этого файла. 📂
        :return: абсолютный путь к директории логов.
        """
        if getattr(sys, "frozen", False):
            exe_dir = os.path.dirname(sys.executable)
            log_dir = os.path.join(exe_dir, "logs")
        else:
            current_dir = os.path.dirname(__file__)
            log_dir = os.path.join(current_dir, "..", "logs")
        os.makedirs(log_dir, exist_ok=True)
        return os.path.abspath(log_dir)
