import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QVBoxLayout

class UserForm(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем метки и поля ввода для имени, фамилии и возраста
        self.name_label = QLabel('Имя:')
        self.name_input = QLineEdit(self)
        self.name_input.setClearButtonEnabled(True)  # Появляется кнопка очистки, если в поле есть текст

        self.surname_label = QLabel('Фамилия:')
        self.surname_input = QLineEdit(self)
        self.surname_input.setClearButtonEnabled(True)

        self.age_label = QLabel('Возраст:')
        self.age_input = QLineEdit(self)
        self.age_input.setClearButtonEnabled(True)

        # Создаем кнопку "Отправить" и подключаем к ней обработчик события
        self.submit_button = QPushButton('Отправить', self)
        self.submit_button.clicked.connect(self.display_info)

        # Создаем формовую компоновку и добавляем в нее метки и поля ввода
        form_layout = QFormLayout()
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.surname_label, self.surname_input)
        form_layout.addRow(self.age_label, self.age_input)
        form_layout.addRow(self.submit_button)

        # Создаем общую компоновку для виджета и устанавливаем ее
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

        self.setWindowTitle('Форма пользователя')

    def display_info(self):
        # Получаем данные из полей ввода и выводим их
        name = self.name_input.text()
        surname = self.surname_input.text()
        age = self.age_input.text()
        print(f"Имя: {name}\nФамилия: {surname}\nВозраст: {age}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserForm()
    window.show()
    sys.exit(app.exec())
