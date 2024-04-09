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
    # Удалим одну из записей студента
    if not query.exec('''
        DELETE FROM Students WHERE id = 1
    '''):
        print('Ошибка при удалении записи:', query.lastError().text())
    else:
        print('Запись успешно удалена')


if __name__ == '__main__':
    createConnection()
    testTrigger()
