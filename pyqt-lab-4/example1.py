import sys
from PyQt6.QtWidgets import (
	QApplication, QWidget, QHBoxLayout, QLabel,
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

		layout = QHBoxLayout()  # Создаем экземпляр менеджера компоновки
		layout.addWidget(self.language_label)  # Добавляем виджет в макет
		layout.addWidget(self.python_radio)
		layout.addWidget(self.java_radio)
		layout.addWidget(self.cpp_radio)
		layout.addWidget(self.show_code_checkbox)
		layout.addWidget(self.submit_button)
		self.setLayout(layout)
		self.setWindowTitle('Выбор языка программирования')
		self.setMinimumWidth(1000)  # Устанавливаем минимальную ширину окна

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
		message_box.setText(
			f"Выбранный язык программирования: {self.selected_language},\nОтображать код: {self.show_code_option}.")
		message_box.exec()
		if message_box == QMessageBox.StandardButton.Ok:
			print("OK!")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = ProgrammingLanguageApp()
	window.show()
	sys.exit(app.exec())
