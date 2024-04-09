# Импорт необходимых модулей
import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class QueryExamples:
    def __init__(self):
        super().__init__()
        self.createConnection()
        self.exampleQueries()

    def createConnection(self):
        """Создание соединения с базой данных."""
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("accounts.db")
        if not database.open():
            print("Невозможно открыть файл источника данных.")
            sys.exit(1)  # Код ошибки 1 - означает ошибку

    def exampleQueries(self):
        """Примеры работы с базой данных."""
        # Конструктор QSqlQuery принимает необязательный
        # объект QSqlDatabase, который указывает, какое
        # соединение с базой данных следует использовать.
        # В данном примере мы не указываем никакого соединения,
        # поэтому используется соединение по умолчанию.
        # При возникновении ошибки функция exec() возвращает false.
        # Ошибка затем доступна в виде SqlQuery::lastError()
        # Выполнение простого запроса
        query = QSqlQuery()
        query.exec("SELECT first_name, last_name FROM \
                    accounts WHERE employee_id > 2000")
        # Навигация по набору результатов
        while query.next():
            f_name = str(query.value(0))
            l_name = str(query.value(1))
            print(f_name, l_name)
        # Вставка одной новой записи в базу данных
        query.exec("""INSERT INTO accounts (
                        employee_id, first_name, last_name,
                        email, department, country_id)
                        VALUES (2134, 'Robert', 'Downey',
                        'downeyr@mail.com', 'Managerial', 1)""")
        # Обновление записи в базе данных
        query.exec("UPDATE accounts SET department = 'R&D' \
                    WHERE employee_id = 2134")
        # Удалить запись из базы данных
        query.exec("DELETE FROM accounts WHERE \
                    employee_id <= 1500")


if __name__ == "__main__":
    QueryExamples()
    sys.exit(0)
