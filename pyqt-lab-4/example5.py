import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QFormLayout

class MultiLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем вертикальную компоновку (QVBoxLayout)
        vertical_layout = QVBoxLayout()
        label1 = QLabel('Вертикальная компоновка')
        input1 = QLineEdit(self)
        button1 = QPushButton('Кнопка 1', self)
        vertical_layout.addWidget(label1)
        vertical_layout.addWidget(input1)
        vertical_layout.addWidget(button1)

        # Создаем горизонтальную компоновку (QHBoxLayout)
        horizontal_layout = QHBoxLayout()
        label2 = QLabel('Горизонтальная компоновка')
        input2 = QLineEdit(self)
        button2 = QPushButton('Кнопка 2', self)
        horizontal_layout.addWidget(label2)
        horizontal_layout.addWidget(input2)
        horizontal_layout.addWidget(button2)

        # Создаем сеточную компоновку (QGridLayout)
        grid_layout = QGridLayout()
        label3 = QLabel('Сеточная компоновка')
        input3 = QLineEdit(self)
        button3 = QPushButton('Кнопка 3', self)
        grid_layout.addWidget(label3, 0, 0)
        grid_layout.addWidget(input3, 0, 1)
        grid_layout.addWidget(button3, 0, 2)

        # Создаем формовую компоновку (QFormLayout)
        form_layout = QFormLayout()
        label4 = QLabel('Формовая компоновка')
        input4 = QLineEdit(self)
        button4 = QPushButton('Кнопка 4', self)
        form_layout.addRow(label4, input4)
        form_layout.addRow(button4)

        # Добавляем все компоновки в общую вертикальную компоновку
        main_layout = QVBoxLayout()
        main_layout.addLayout(vertical_layout)
        main_layout.addLayout(horizontal_layout)
        main_layout.addLayout(grid_layout)
        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)
        self.setWindowTitle('Пример с несколькими компоновками')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultiLayoutExample()
    window.show()
    sys.exit(app.exec())
