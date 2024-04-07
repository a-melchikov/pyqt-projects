import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedLayout

class SwitchableWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем виджеты для страницы 1 и страницы 2
        self.page1_label = QLabel('Это страница 1')
        self.page1_button = QPushButton('Переключить на страницу 2')
        self.page1_button.clicked.connect(self.switch_to_page2)

        self.page2_label = QLabel('Это страница 2')
        self.page2_button = QPushButton('Переключить на страницу 1')
        self.page2_button.clicked.connect(self.switch_to_page1)

        # Создаем QStackedLayout для управления видимостью страниц
        self.stacked_layout = QStackedLayout()

        # Добавляем виджеты страниц в QStackedLayout
        self.stacked_layout.addWidget(self.page1_widget())
        self.stacked_layout.addWidget(self.page2_widget())

        # Устанавливаем QStackedLayout как макет виджета
        self.setLayout(self.stacked_layout)

    def page1_widget(self):
        # Создаем виджет для страницы 1 и настраиваем его макет
        page1_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.page1_label)
        layout.addWidget(self.page1_button)
        page1_widget.setLayout(layout)
        return page1_widget

    def page2_widget(self):
        # Создаем виджет для страницы 2 и настраиваем его макет
        page2_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.page2_label)
        layout.addWidget(self.page2_button)
        page2_widget.setLayout(layout)
        return page2_widget

    def switch_to_page2(self):
        # Переключаемся на страницу 2
        self.stacked_layout.setCurrentIndex(1)

    def switch_to_page1(self):
        # Переключаемся на страницу 1
        self.stacked_layout.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SwitchableWidget()
    window.show()
    sys.exit(app.exec())
