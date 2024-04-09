import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('university.db')
    if not db.open():
        print('Невозможно открыть базу данных')
        sys.exit(1)


def testTrigger():
    query = QSqlQuery()

    # Выведем данные перед обновлением faculty_id
    print("Данные до обновления faculty_id:")
    query.exec('SELECT * FROM Students WHERE id = 2')
    while query.next():
        print(
            f"Студент {query.value('first_name')} {query.value('last_name')}, faculty_id: {query.value('faculty_id')}")

    # Обновляем faculty_id для одной из записей студентов
    if not query.exec('''
        UPDATE Students SET faculty_id = 2 WHERE id = 2
    '''):
        print('Ошибка при обновлении faculty_id:', query.lastError().text())

    # Выведем данные после обновления faculty_id
    print("\nДанные после обновления faculty_id:")
    query.exec('SELECT * FROM Students WHERE id = 2')
    while query.next():
        print(
            f"Студент {query.value('first_name')} {query.value('last_name')}, faculty_id: {query.value('faculty_id')}")


if __name__ == '__main__':
    createConnection()
    testTrigger()
