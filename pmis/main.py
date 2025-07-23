# pmis/main.py
# Точка входа: запуск QApplication, чтение конфигов, старт главного окна
from utils.logger import LoggerManager
from init_proj.init_proj import InitProj

class App:
    """
    Основной класс приложения.
    Загружает настройки, запускает модули и логирует их успешную работу.
    """
    def __init__(self):
        # Настройка логирования
        self.logger = LoggerManager(__name__).get_logger()

        # Автоматический запуск приложения
        self.run()

    def run(self):
        init = InitProj()

if __name__ == "__main__":
    app = App()
