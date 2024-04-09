# create_database.py
# Импорт необходимых модулей
import sys
import random
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class CreateEmployeeData:
    """Создаем пример базы данных для проекта.
    Класс демонстрирует, как подключаться к базе данных, создавать
    запросы, создавать таблицы и записи в этих таблицах."""

    # Создаем соединение с базой данных. Если файл db
    # не существует, будет создан новый файл db.
    # Использовать драйвер SQLite версии 3
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("accounts.db")
    if not database.open():
        print("Невозможно открыть файл источника данных.")
        sys.exit(1)  # Код ошибки 1 - означает ошибку
    query = QSqlQuery()
    # Стирание содержимого базы данных
    query.exec("DROP TABLE accounts")
    query.exec("DROP TABLE countries")
    query.exec("""CREATE TABLE accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        employee_id INTEGER NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(40) NOT NULL,
        department VARCHAR(20) NOT NULL,
        country_id VARCHAR(20) REFERENCES countries(id))""")
    # Позиционная привязка для вставки записей в базу данных
    query.prepare("""INSERT INTO accounts (
        employee_id, first_name, last_name,
        email, department, country_id)
        VALUES (?, ?, ?, ?, ?, ?)""")
    first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia",
                   "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail",
                   "Valorie", "Teesha", "Jazzmin", "Liam", "Noah",
                   "William", "James", "Logan", "Benjamin", "Mason",
                   "Elijah", "Oliver", "Jason", "Lucas", "Michael"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                  "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
                  "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
                  "Perez", "Thompson", "White", "Harris"]
    # Создайте данные для первой таблицы, account
    employee_ids = random.sample(range(1000, 2500), len(first_names))
    countries = {"Russia": 1, "India": 2, "China": 3,
                 "France": 4, "Germany": 5}
    country_names = list(countries.keys())
    country_codes = list(countries.values())
    departments = ["Production", "R&D", "Marketing", "HR",
                   "Finance", "Engineering", "Managerial"]
    for f_name in first_names:
        l_name = last_names.pop()
        email = (l_name + f_name[0]).lower() + "@mail.ru"
        country_id = random.choice(country_codes)
        dept = random.choice(departments)
        employee_id = employee_ids.pop()
        query.addBindValue(employee_id)
        query.addBindValue(f_name)
        query.addBindValue(l_name)
        query.addBindValue(email)
        query.addBindValue(dept)
        query.addBindValue(country_id)
        query.exec()
    # Создайте данные для второй таблицы, стран
    country_query = QSqlQuery()
    country_query.exec("""CREATE TABLE countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        country VARCHAR(20) NOT NULL)""")
    country_query.prepare("INSERT INTO countries (country) VALUES (?)")
    for name in country_names:
        country_query.addBindValue(name)
        country_query.exec()
    print("[INFO] Database successfully created.")


if __name__ == "__main__":
    CreateEmployeeData()
    sys.exit(0)
