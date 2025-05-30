# init_proj_ui/init_proj_ui.py

import os  # 😊 для работы с путями
from PyQt6 import uic, QtWidgets  # 😊 Qt Designer UI и виджеты
from utils.logger import LoggerManager  # 😊 централизованное логирование


class InitWindow(QtWidgets.QMainWindow):
    """
    Главное окно приложения с выпадающим списком (ComboBox).
    """
    def __init__(self) -> None:
        super().__init__()
        # Инициализация логера
        self.logger = LoggerManager(__name__).get_logger()  # 😊 создаём логгер для окна

        # Получаем путь до .ui-файла
        root_dir: str = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir)
        )  # 😊 корень проекта

        ui_path: str = os.path.join(
            root_dir,
            "init_proj",
            "init_proj.ui"
        )  # 😊 путь до UI
        uic.loadUi(ui_path, self)  # 😊 загружаем форму
        self.logger.info("UI загружен для InitWindow")

    #     # Заполняем ComboBox примерами
    #     items: list[str] = ["Москва", "Петербург", "Казань"]
    #     self.comboBox.addItems(items)  # 😊 добавляем пункты
    #
    #     # Связываем сигнал изменения выбора
    #     self.comboBox.currentTextChanged.connect(self.on_selection_changed)
    #
    # def on_selection_changed(self, text: str) -> None:
    #     """
    #     Обработчик изменения текста в ComboBox.
    #
    #     Args:
    #         text (str): Новый выбранный элемент.
    #     """
    #     self.logger.info(f"Выбрано: {text}")  # 😊 логируем выбор