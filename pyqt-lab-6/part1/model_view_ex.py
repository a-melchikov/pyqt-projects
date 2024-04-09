# model_view_ex.py
# Import necessary modules
import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout)
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка графического интерфейса приложения."""
        self.setGeometry(100, 100, 480, 300)
        self.setWindowTitle("Пример модели и представления")
        self.setupMainWindow()
        self.loadCSVFile()
        self.show()

    def setupMainWindow(self):
        """Создаем и располагаем виджеты в главном окне."""
        self.model = QStandardItemModel()
        table_view = QTableView()
        table_view.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        table_view.setModel(self.model)
        # Установите начальные значения строк и столбцов
        self.model.setRowCount(8)
        self.model.setColumnCount(4)
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        self.setLayout(main_v_box)

    def loadCSVFile(self):
        """Загрузить заголовок и строки из CSV-файла."""
        file_name = "input.csv"
        with open(file_name, "r") as csv_f:
            reader = csv.reader(csv_f)
            header_labels = next(reader)
            self.model.setHorizontalHeaderLabels(header_labels)
            for i, row in enumerate(csv.reader(csv_f)):
                items = [QStandardItem(item) for item in row]
                self.model.insertRow(i, items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
