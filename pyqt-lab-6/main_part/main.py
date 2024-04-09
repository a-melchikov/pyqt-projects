import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QTableView,
    QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox, QHeaderView, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtSql import (
    QSqlDatabase, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("University Database Management System")
        self.createConnection()
        self.createModel()
        self.setUpMainWindow()
        self.show()

    def createConnection(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('university.db')
        if not db.open():
            print('Невозможно открыть базу данных')
            sys.exit(1)

        # Проверить, существуют ли в базе данных нужные нам таблицы
        tables_needed = {"Disciplines", "Faculties"}
        tables_not_found = tables_needed - set(db.tables())
        if tables_not_found:
            QMessageBox.critical(
                None, "Ошибка",
                f"""<p>The following tables are missing
                    from the database: {tables_not_found}</p>"""
            )
            sys.exit(1)  # Код ошибки 1 - означает ошибку


    def createModel(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("Students")
        self.model.setEditStrategy(QSqlRelationalTableModel.EditStrategy.OnFieldChange)
        self.model.setRelation(self.model.fieldIndex("faculty_id"), QSqlRelation("Faculties", "id", "faculty_name"))
        self.model.setRelation(self.model.fieldIndex("discipline_id"), QSqlRelation("Disciplines", "id", "subject"))

        # Установка заголовков для красивых имен
        self.model.setHeaderData(self.model.fieldIndex("id"), Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex("first_name"), Qt.Orientation.Horizontal, "First Name")
        self.model.setHeaderData(self.model.fieldIndex("last_name"), Qt.Orientation.Horizontal, "Last Name")
        self.model.setHeaderData(self.model.fieldIndex("course"), Qt.Orientation.Horizontal, "Course")
        self.model.setHeaderData(self.model.fieldIndex("faculty_id"), Qt.Orientation.Horizontal, "Faculty")
        self.model.setHeaderData(self.model.fieldIndex("discipline_id"), Qt.Orientation.Horizontal, "Discipline")
        self.model.setHeaderData(self.model.fieldIndex("group_number"), Qt.Orientation.Horizontal, "Group Number")

        self.model.select()

    def setUpMainWindow(self):
        title = QLabel("University Database Management System")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font: bold 24px")

        # Кнопка "Добавить студента"
        add_student_button = QPushButton("Добавить студента")
        add_student_button.setIcon(QIcon(os.path.join("icons", "add.png")))
        add_student_button.setStyleSheet("padding: 10px")
        add_student_button.clicked.connect(self.addRecord)

        # Кнопка "Удалить"
        delete_button = QPushButton("Удалить")
        delete_button.setIcon(QIcon(os.path.join("icons", "delete.png")))
        delete_button.setStyleSheet("padding: 10px")
        delete_button.clicked.connect(self.deleteRecord)

        # Настройка комбо-бокса для выбора параметра сортировки
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Sort by ID", "Sort by First Name", "Sort by Last Name",
                                  "Sort by Сourse", "Sort by Discipline", "Sort by Faculty",
                                  "Sort by Group number"])
        self.sort_combo.currentIndexChanged.connect(self.setSortingOrder)

        h_box = QHBoxLayout()
        h_box.addWidget(add_student_button)
        h_box.addWidget(delete_button)
        h_box.addStretch()

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Инстанцирование делегата
        delegate = QSqlRelationalDelegate()
        self.table_view.setItemDelegate(delegate)

        v_box = QVBoxLayout()
        v_box.addWidget(title)
        v_box.addWidget(self.sort_combo)
        v_box.addWidget(QLabel())  # Пустой виджет для создания пространства между заголовком и таблицей
        v_box.addLayout(h_box)
        v_box.addWidget(self.table_view)

        self.setLayout(v_box)

    def addRecord(self):
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)

    def deleteRecord(self):
        reply = QMessageBox.question(self, 'Подтверждение удаления',
                                     'Вы уверены, что хотите удалить эту запись?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            current_row = self.table_view.currentIndex().row()
            if current_row >= 0:
                self.model.removeRow(current_row)
                self.model.select()
            else:
                QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите запись для удаления",
                                    QMessageBox.StandardButton.Ok)

    def setSortingOrder(self):
        """Установка сортировки для основной таблицы."""
        sort_option = self.sort_combo.currentText()
        if sort_option == "Sort by ID":
            self.model.setSort(self.model.fieldIndex("id"), Qt.SortOrder.AscendingOrder)
        elif sort_option == "Sort by First Name":
            self.model.setSort(self.model.fieldIndex("first_name"), Qt.SortOrder.AscendingOrder)
        elif sort_option == "Sort by Last Name":
            self.model.setSort(self.model.fieldIndex("last_name"), Qt.SortOrder.AscendingOrder)
        elif sort_option == "Sort by Сourse":
            self.model.setSort(self.model.fieldIndex("course"), Qt.SortOrder.AscendingOrder)
        elif sort_option == "Sort by Discipline":
            self.model.setSort(self.model.fieldIndex("discipline_id"), Qt.SortOrder.AscendingOrder)
        elif sort_option == "Sort by Faculty":
            self.model.setSort(self.model.fieldIndex("faculty_id"), Qt.SortOrder.AscendingOrder)
        elif sort_option == "Sort by Group number":
            self.model.setSort(self.model.fieldIndex("group_number"), Qt.SortOrder.AscendingOrder)
        self.model.select()  # Применение сортировки


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
