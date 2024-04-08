import sys

from PyQt6.QtCore import QDateTime
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

        # Создаем метку для отображения общей суммы
        self.total_amount_label = QLabel('Общая сумма: 0.00')
        main_layout.addWidget(self.total_amount_label)

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
        self.date_input.setDateTime(QDateTime.currentDateTime())
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

        # Подключаем метод сброса настроек к сигналу нажатия кнопки "Сброс"
        self.reset_button.clicked.connect(self.reset_settings)

        # Подключаем метод удаления записей к сигналу нажатия кнопки "Удалить запись"
        self.delete_record_button.clicked.connect(self.delete_record)

        # Подключаем метод добавления записей к сигналу нажатия кнопки "Добавить запись"
        self.add_record_button.clicked.connect(self.add_record)

        # Подключаем метод обновления общей суммы к сигналу нажатия кнопки "Добавить запись"
        self.add_record_button.clicked.connect(self.update_total_amount)

        main_layout.addLayout(button_layout)  # Добавляем компоновку кнопок в общую компоновку
        self.setLayout(main_layout)  # Устанавливаем общую компоновку для окна

    def update_total_amount(self):
        total_amount = 0
        for row in range(self.table_widget.rowCount()):
            amount_item = self.table_widget.item(row, 0)  # Получаем ячейку с суммой расходов
            if amount_item:
                total_amount += float(amount_item.text())  # Суммируем суммы расходов
        self.total_amount_label.setText(f'Общая сумма: {total_amount:.2f}')

    def add_record(self):
        # Получаем данные из полей ввода
        amount = self.amount_input.text()
        category = self.category_combobox.currentText()
        date = self.date_input.dateTime().toString('dd.MM.yyyy')

        # Создаем новую строку для таблицы и заполняем ее данными
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(amount))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem(category))
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(date))

        # Очищаем поля ввода
        self.amount_input.clear()
        self.category_combobox.setCurrentIndex(0)
        self.date_input.setDateTime(self.date_input.minimumDateTime())

    def delete_record(self):
        selected_rows = set()  # Создаем множество для хранения индексов выбранных строк
        for item in self.table_widget.selectedItems():
            selected_rows.add(item.row())  # Добавляем индекс выбранной строки в множество

        # Удаляем выбранные строки из таблицы
        for row in sorted(selected_rows, reverse=True):
            self.table_widget.removeRow(row)

        # Обновляем общую сумму после удаления записей
        self.update_total_amount()

    def reset_settings(self):
        # Удаляем все записи из таблицы
        self.table_widget.setRowCount(0)

        # Обновляем общую сумму после сброса настроек
        self.update_total_amount()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseCalculator()
    window.show()
    sys.exit(app.exec())
