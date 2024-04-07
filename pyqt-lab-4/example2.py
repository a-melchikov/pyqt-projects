import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel,
    QRadioButton, QCheckBox, QPushButton, QMessageBox
)

class ProgrammingLanguageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.language_label = QLabel('Выберите язык программирования:')
        self.python_radio = QRadioButton('Python')
        self.java_radio = QRadioButton('Java')
        self.cpp_radio = QRadioButton('C++')
        self.show_code_checkbox = QCheckBox('Отображать код', self)
        self.submit_button = QPushButton('Подтвердить', self)
        self.submit_button.clicked.connect(self.display_selection)

        layout = QGridLayout()
        layout.addWidget(self.language_label, 0, 0, 1, 3)
        layout.addWidget(self.python_radio, 1, 0)
        layout.addWidget(self.java_radio, 1, 1)
        layout.addWidget(self.cpp_radio, 1, 2)
        layout.addWidget(self.show_code_checkbox, 2, 0, 1, 2)
        layout.addWidget(self.submit_button, 2, 2)
        self.setLayout(layout)
        self.setWindowTitle('Выбор языка программирования')
        self.selected_language = None
        self.show_code_option = None

    def display_selection(self):
        if self.python_radio.isChecked():
            self.selected_language = 'Python'
        elif self.java_radio.isChecked():
            self.selected_language = 'Java'
        elif self.cpp_radio.isChecked():
            self.selected_language = 'C++'
        self.show_code_option = self.show_code_checkbox.isChecked()
        print("Выбранный язык программирования:", self.selected_language)
        print("Отображать код:", self.show_code_option)
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Информационное сообщение")
        message_box.setIcon(QMessageBox.Icon.Information)
        message_box.setText(f"Выбранный язык программирования: {self.selected_language},\nОтображать код: {self.show_code_option}.")
        message_box.exec()
        if message_box == QMessageBox.StandardButton.Ok:
            print("OK!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgrammingLanguageApp()
    window.show()
    sys.exit(app.exec())
