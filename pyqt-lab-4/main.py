import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, \
	QTableWidgetItem, QHeaderView, QLabel, QLineEdit, QComboBox, QDateTimeEdit


class ExpenseCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Калькулятор расходов')
        self.resize(600, 400)  # Устанавливаем размер окна

        self.init_ui()  # Инициализируем пользовательский интерфейс

    def init_ui(self):
        # Создаем компоновку для размещения виджетов
        main_layout = QVBoxLayout()

        # Создаем таблицу для отображения данных
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)  # Устанавливаем количество столбцов
        self.table_widget.setHorizontalHeaderLabels(['Сумма', 'Категория', 'Дата'])

        # Растягиваем все столбцы равномерно
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        main_layout.addWidget(self.table_widget)

        # Создаем компоновку для кнопок
        button_layout = QHBoxLayout()

        # Создаем компоновку для полей ввода
        input_layout = QHBoxLayout()

        # Поле ввода для суммы
        self.amount_label = QLabel('Сумма:')
        self.amount_input = QLineEdit()
        input_layout.addWidget(self.amount_label)
        input_layout.addWidget(self.amount_input)

        # Поле выбора категории
        self.category_label = QLabel('Категория:')
        self.category_combobox = QComboBox()
        self.category_combobox.addItems(['Продукты', 'Развлечения', 'Транспорт', 'Жилье', 'Здоровье', 'Прочее'])
        input_layout.addWidget(self.category_label)
        input_layout.addWidget(self.category_combobox)

        # Поле ввода даты
        self.date_label = QLabel('Дата:')
        self.date_input = QDateTimeEdit()
        input_layout.addWidget(self.date_label)
        input_layout.addWidget(self.date_input)

        main_layout.addLayout(input_layout)  # Добавляем компоновку полей ввода в общую компоновку

        # Создаем кнопку "Добавить запись"
        self.add_record_button = QPushButton('Добавить запись')
        button_layout.addWidget(self.add_record_button)

        # Создаем кнопку "Удалить запись"
        self.delete_record_button = QPushButton('Удалить запись')
        button_layout.addWidget(self.delete_record_button)

        # Создаем кнопку "Сброс"
        self.reset_button = QPushButton('Сброс')
        button_layout.addWidget(self.reset_button)

        main_layout.addLayout(button_layout)  # Добавляем компоновку кнопок в общую компоновку

        self.setLayout(main_layout)  # Устанавливаем общую компоновку для окна


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseCalculator()
    window.show()
    sys.exit(app.exec())
