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
    # Попытка вставить запись с недопустимым значением курса
    if not query.exec('''
        INSERT INTO Students (first_name, last_name, course, discipline_id, faculty_id, group_number)
        VALUES ('John', 'Doe', 6, 1, 1, '101')
    '''):
        print('Ошибка при вставке записи:', query.lastError().text())
    else:
        print('Запись успешно вставлена')

if __name__ == '__main__':
    createConnection()
    testTrigger()
