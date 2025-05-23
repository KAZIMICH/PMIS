# common/logger.py
# Здесь расположен реализованный централизованный логгер

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
import textwrap  # для выравнивания HTML-шаблона
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

    def format(self, record):
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

    def __init__(self, datefmt=None):
        super().__init__(fmt="%(message)s", datefmt=datefmt)

    def format(self, record):
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
            .info { color: yellow; }
            .error { color: red; }
            .warning { color: orange; }
            .debug { color: gray; }
          </style>
        </head>
        <body>
          <h1>Логи приложения</h1>
        """
    )
    FOOTER = textwrap.dedent("""
            </body>
            </html>
            """
    )

    def emit(self, record):
            if self.stream.tell() == 0:
                self.stream.write(self.HEADER)
            msg = self.format(record)
            self.stream.write(msg)
            self.flush()

    def doRollover(self):
        super().doRollover()
        # следующий emit() снова добавит HEADER 🔄


def setup_logging(module_name: str):
    """
    Настройка логгера:
      - цветной вывод в консоль;
      - вывод в HTML-файл всегда.
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        return logger

    console_fmt = "%(asctime)s - [%(name)s] - %(levelname)s - %(message)s"
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        ColoredFormatter(console_fmt, datefmt="%H:%M:%S")
    )
    logger.addHandler(console_handler)

    log_dir = get_log_dir()
    html_path = os.path.join(log_dir, "app.html")
    html_handler = HtmlFileHandler(
        html_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    html_handler.setLevel(logging.INFO)
    html_handler.setFormatter(
        HtmlFormatter(datefmt="%Y-%m-%d %H:%M:%S")
    )
    logger.addHandler(html_handler)

    return logger


def get_log_dir():
    """
    Директория для логов:
      - рядом с .exe, если скомпилировано;
      - иначе — ../logs. 📂
    """
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        log_dir = os.path.join(exe_dir, "logs")
    else:
        log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)
    return os.path.abspath(log_dir)
