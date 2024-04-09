# account_manager.py
# Импорт необходимых модулей
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QComboBox, QTableView,
    QHeaderView, QAbstractItemView,
    QMessageBox, QHBoxLayout, QVBoxLayout,
    QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtSql import (
    QSqlDatabase, QSqlQuery,
    QSqlRelation, QSqlRelationalTableModel,
    QSqlRelationalDelegate
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка графического интерфейса приложения."""
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("Графический интерфейс управления счетами")
        self.createConnection()
        self.createModel()
        self.setUpMainWindow()
        self.show()

    def createConnection(self):
        """Установите соединение с базой данных.
        Проверьте наличие необходимых таблиц."""
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("accounts.db")
        if not database.open():
            print("Невозможно открыть файл источника данных.")
            sys.exit(1)  # Код ошибки 1 - означает ошибку

        # Проверить, существуют ли в базе данных нужные нам таблицы
        tables_needed = {"accounts", "countries"}
        tables_not_found = tables_needed - set(database.tables())
        if tables_not_found:
            QMessageBox.critical(
                None, "Ошибка",
                f"""<p>The following tables are missing
                from the database: {tables_not_found}</p>"""
            )
            sys.exit(1)  # Код ошибки 1 - означает ошибку

    def createModel(self):
        """Настройка модели и заголовков, заполнение модели."""
        self.model = QSqlRelationalTableModel()
        self.model.setTable("accounts")
        self.model.setRelation(self.model.fieldIndex("country_id"),
                               QSqlRelation("countries", "id", "country"))
        self.model.setHeaderData(self.model.fieldIndex("id"),
                                 Qt.Orientation.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex("employee_id"),
                                 Qt.Orientation.Horizontal, "Employee ID")
        self.model.setHeaderData(self.model.fieldIndex("first_name"),
                                 Qt.Orientation.Horizontal, "First")
        self.model.setHeaderData(self.model.fieldIndex("last_name"),
                                 Qt.Orientation.Horizontal, "Last")
        self.model.setHeaderData(self.model.fieldIndex("email"),
                                 Qt.Orientation.Horizontal, "E-mail")
        self.model.setHeaderData(self.model.fieldIndex("department"),
                                 Qt.Orientation.Horizontal, "Dept.")
        self.model.setHeaderData(self.model.fieldIndex("country_id"),
                                 Qt.Orientation.Horizontal, "Country")

        # Наполнение модели данными
        self.model.select()

    def setUpMainWindow(self):
        """Создание и расположение виджетов в главном окне."""
        icons_path = ""
        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Policy.Fixed,
                            QSizePolicy.Policy.Fixed)
        title.setStyleSheet("font: bold 24px")
        add_product_button = QPushButton("Добавить сотрудника")
        add_product_button.setIcon(QIcon(os.path.join(
            icons_path, "add.png")))
        add_product_button.setStyleSheet("padding: 10px")
        add_product_button.clicked.connect(self.addItem)
        del_product_button = QPushButton("Удалить")
        del_product_button.setIcon(QIcon(os.path.join(
            icons_path, "delete.png")))
        del_product_button.setStyleSheet("padding: 10px")
        del_product_button.clicked.connect(self.deleteItem)

        # Настройка сортировочного комбобокса
        sorting_options = [
            "Sort by ID", "Sort by Employee ID",
            "Sort by First Name", "Sort by Last Name",
            "Sort by Department", "Sort by Country"
        ]
        sort_combo = QComboBox()
        sort_combo.addItems(sorting_options)
        sort_combo.currentTextChanged.connect(self.setSortingOrder)

        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_product_button)
        buttons_h_box.addWidget(del_product_button)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_combo)

        # Виджет, содержащий кнопки редактирования
        edit_container = QWidget()
        edit_container.setLayout(buttons_h_box)

        # Создание табличного представления и установка модели
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        horizontal = self.table_view.horizontalHeader()
        horizontal.setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        vertical = self.table_view.verticalHeader()
        vertical.setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        self.table_view.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection)
        self.table_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)

        # Инстанцирование делегата
        delegate = QSqlRelationalDelegate()
        self.table_view.setItemDelegate(delegate)

        # Основной макет
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(
            title, Qt.AlignmentFlag.AlignLeft)
        main_v_box.addWidget(edit_container)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def addItem(self):
        """Добавить новую запись в последнюю строку таблицы."""
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)
        query = QSqlQuery()
        query.exec("SELECT MAX (id) FROM accounts")
        if query.next():
            int(query.value(0))

    def deleteItem(self):
        """Удаление всей строки из таблицы."""
        current_item = self.table_view.selectedIndexes()
        for index in current_item:
            self.model.removeRow(index.row())
            self.model.select()

    def setSortingOrder(self, text):
        """Сортировка строк в таблице."""
        if text == "Sort by ID":
            self.model.setSort(self.model.fieldIndex("id"),
                               Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Employee ID":
            self.model.setSort(self.model.fieldIndex("employee_id"),
                               Qt.SortOrder.AscendingOrder)
        elif text == "Sort by First Name":
            self.model.setSort(self.model.fieldIndex("first_name"),
                               Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Last Name":
            self.model.setSort(self.model.fieldIndex("last_name"),
                               Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Department":
            self.model.setSort(self.model.fieldIndex("department"),
                               Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Country":
            self.model.setSort(self.model.fieldIndex("country"),
                               Qt.SortOrder.AscendingOrder)
        self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
