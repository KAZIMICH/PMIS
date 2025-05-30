# init_proj/init_proj.py
import sys  # 😊 для работы с аргументами командной строки
from utils.logger import LoggerManager  # 😊 централизованное логирование
from PyQt6 import QtWidgets  # 😊 основные виджеты Qt
from init_proj.init_proj_ui import InitWindow  # 😊 импорт главного окна


class InitProj:
    """
    Класс инициализации проекта: настройка логирования и запуск GUI.
    """

    def __init__(self) -> None:
        # Настройка логирования
        self.logger = LoggerManager(__name__).get_logger()  # 😊 создаём логгер
        self.logger.info("Запуск InitProj")

        try:
            self.gui_run()
        except Exception:
            self.logger.exception("Необработанное исключение при инициализации GUI")  # 😊 логируем стектрейс
            raise  # пробрасываем для внешнего анализа

    def init_proj(self) -> None:
        """
        Бизнес-логика инициализации проекта.
        """
        self.logger.debug("Выполнен init_proj()")
        # TODO: реализовать логику
        pass

    def gui_run(self) -> None:
        """
        Создаёт QApplication и показывает главное окно.
        """
        # Создаём приложение Qt
        app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)  # 😊

        # Создаём и показываем главное окно
        window: InitWindow = InitWindow()  # 😊
        window.show()  # 😊

        self.logger.info("Главное окно отображено")
        sys.exit(app.exec())  # 😊 старт цикла событий

    def get_data(self) -> None:
        """
        Получение необходимых данных для инициализации.
        """
        self.logger.debug("Вызван get_data()")
        # TODO: реализовать сбор данных
        pass


if __name__ == "__main__":
    InitProj()  # 😊 старт приложения
