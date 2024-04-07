import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QRadioButton, QPushButton, QMessageBox


class WeightCalculator(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()

	def initializeUI(self):
		self.setWindowTitle('Калькулятор веса на других планетах')
		self.setGeometry(100, 100, 420, 250)

		self.weight_input = QLineEdit(self)
		self.weight_input.setPlaceholderText('Введите ваш вес')

		self.planet_radio_buttons = []
		self.planet_names = ['Меркурий', 'Венера', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
		for planet in self.planet_names:
			radio_button = QRadioButton(planet, self)
			self.planet_radio_buttons.append(radio_button)

		self.calculate_button = QPushButton('Рассчитать', self)
		self.calculate_button.clicked.connect(self.calculateWeight)

		layout = QVBoxLayout()
		layout.addWidget(self.weight_input)
		for radio_button in self.planet_radio_buttons:
			layout.addWidget(radio_button)
		layout.addWidget(self.calculate_button)

		self.setLayout(layout)

	def calculateWeight(self):
		weight = float(self.weight_input.text())
		selected_planet = None
		for radio_button in self.planet_radio_buttons:
			if radio_button.isChecked():
				selected_planet = radio_button.text()
				break

		if selected_planet:
			gravity_ratios = {
				'Меркурий': 0.378,
				'Венера': 0.907,
				'Марс': 0.377,
				'Юпитер': 2.364,
				'Сатурн': 0.916,
				'Уран': 0.889,
				'Нептун': 1.12,
			}
			weight_on_selected_planet = weight * gravity_ratios[selected_planet]
			message_box = QMessageBox()
			message_box.setWindowTitle('Результат')
			message_box.setText(f'Ваш вес на планете {selected_planet}: {weight_on_selected_planet:.2f} кг')
			message_box.exec()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = WeightCalculator()
	window.show()
	sys.exit(app.exec())
