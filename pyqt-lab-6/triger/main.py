import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication


def createTrigger():
	# Устанавливаем соединение с базой данных
	db = QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('example.db')
	if not db.open():
		print('Невозможно открыть базу данных')
		sys.exit(1)

	# Создаем объект запроса
	query = QSqlQuery()

	# Создаем триггер (здесь приведен пример для SQLite)
	trigger_query = '''
    CREATE TRIGGER IF NOT EXISTS my_trigger
    AFTER INSERT ON my_table
    FOR EACH ROW
    BEGIN
    -- Ваш SQL-код триггера здесь
    -- Например, можно выполнить дополнительные SQL-запросы
    -- Или вызвать функцию или процедуру
    END;
    '''

	# Выполняем запрос
	if not query.exec(trigger_query):
		print('Ошибка создания триггера:', query.lastError().text())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	createTrigger()
	sys.exit(app.exec())
