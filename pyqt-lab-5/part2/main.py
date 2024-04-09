import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from calculator import Ui_Form  # Импортируем класс Ui_Form из модуля calculator

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Создаем экземпляр пользовательского интерфейса из класса Ui_Form
        self.ui.setupUi(self)  # Настройка пользовательского интерфейса, передача self в качестве родительского виджета
        self.expression = ""  # Переменная для хранения текущего выражения
        # Привязываем обработчики событий для всех кнопок калькулятора
        self.ui.button_0.clicked.connect(lambda: self.append_number("0"))
        self.ui.button_1.clicked.connect(lambda: self.append_number("1"))
        self.ui.button_2.clicked.connect(lambda: self.append_number("2"))
        self.ui.button_3.clicked.connect(lambda: self.append_number("3"))
        self.ui.button_4.clicked.connect(lambda: self.append_number("4"))
        self.ui.button_5.clicked.connect(lambda: self.append_number("5"))
        self.ui.button_6.clicked.connect(lambda: self.append_number("6"))
        self.ui.button_7.clicked.connect(lambda: self.append_number("7"))
        self.ui.button_8.clicked.connect(lambda: self.append_number("8"))
        self.ui.button_9.clicked.connect(lambda: self.append_number("9"))
        self.ui.button_dot.clicked.connect(lambda: self.append_number("."))
        self.ui.button_plus.clicked.connect(lambda: self.append_operator("+"))
        self.ui.button_minus.clicked.connect(lambda: self.append_operator("-"))
        self.ui.button_mul.clicked.connect(lambda: self.append_operator("*"))
        self.ui.button_div.clicked.connect(lambda: self.append_operator("/"))
        self.ui.button_change_sign.clicked.connect(self.change_sign)  # Связываем кнопку с методом изменения знака
        self.ui.button_backspace.clicked.connect(self.backspace)  # Связываем кнопку с методом удаления последнего символа
        self.ui.button_clear.clicked.connect(self.clear)  # Связываем кнопку с методом очистки выражения
        self.ui.button_equal.clicked.connect(self.calculate)  # Связываем кнопку с методом вычисления результата
        self.show()  # Отображаем окно приложения

    def append_number(self, number):
        self.expression += number  # Добавляем число к текущему выражению
        self.update_display()  # Обновляем отображение

    def append_operator(self, operator):
        if self.expression and self.expression[-1] not in "+-*/":
            self.expression += operator  # Добавляем оператор к текущему выражению, если последний символ не является оператором
            self.update_display()

    def change_sign(self):
        if self.expression:
            if self.expression[0] == "-":
                self.expression = self.expression[1:]  # Удаляем знак минуса, если он уже присутствует
            else:
                self.expression = "-" + self.expression  # Добавляем знак минуса, если его нет
            self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]  # Удаляем последний символ из текущего выражения
        self.update_display()

    def clear(self):
        self.expression = ""  # Очищаем текущее выражение
        self.update_display()

    def calculate(self):
        try:
            result = eval(self.expression)  # Вычисляем результат выражения
            self.expression = str(result)  # Преобразуем результат в строку
            self.update_display()  # Обновляем отображение
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Invalid expression: {e}")  # Выводим сообщение об ошибке, если выражение некорректно
            self.clear()  # Очищаем текущее выражение

    def update_display(self):
        self.ui.lineEdit.setText(self.expression)  # Обновляем текстовое поле с текущим выражением

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаем экземпляр приложения PyQt
    calculator_app = CalculatorApp()  # Создаем экземпляр приложения калькулятора
    sys.exit(app.exec())  # Запускаем цикл обработки событий приложения
