# Импорт необходимых модулей
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableView,
    QMessageBox, QHeaderView, QVBoxLayout
)
from PyQt6.QtSql import (
    QSqlDatabase, QSqlRelation,
    QSqlRelationalTableModel, QSqlRelationalDelegate
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка графического интерфейса приложения."""
        self.setMinimumSize(650, 500)
        self.setWindowTitle("Модель реляционной таблицы")
        self.createConnection()
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
                None, "Error",
                f"""<p>The following tables are missing
                from the database: {tables_not_found}</p>"""
            )
            sys.exit(1)  # Код ошибки 1 - означает ошибку

    def setUpMainWindow(self):
        """Создание и расположение виджетов в главном окне."""
        # Создание модели
        model = QSqlRelationalTableModel()
        model.setTable("accounts")

        # Настройка отношений для внешних ключей
        model.setRelation(
            model.fieldIndex("country_id"),
            QSqlRelation("countries", "id", "country")
        )

        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Наполнение модели данными
        model.select()

        # Создание вертикального макета и добавление виджетов
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)

        # Инстанцирование делегата
        delegate = QSqlRelationalDelegate()
        table_view.setItemDelegate(delegate)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
