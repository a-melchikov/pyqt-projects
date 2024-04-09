import sys
import random
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


# Создание соединения с базой данных
def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('university.db')
    if not db.open():
        print('Невозможно открыть базу данных')
        sys.exit(1)


# Создание таблиц и заполнение данными
def createTablesAndData():
    query = QSqlQuery()
    query.exec('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            course INTEGER NOT NULL,
            discipline_id INTEGER REFERENCES Disciplines(id),
            faculty_id INTEGER REFERENCES Faculties(id),
            group_number VARCHAR(10)
        )
    ''')
    query.exec('''
        CREATE TABLE IF NOT EXISTS Disciplines (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            subject VARCHAR(50) NOT NULL
        )
    ''')
    query.exec('''
        CREATE TABLE IF NOT EXISTS Faculties (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            faculty_name VARCHAR(50) NOT NULL
        )
    ''')

    # Заполнение таблиц случайными данными
    first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    subjects = ["Math", "Physics", "Chemistry", "Biology", "History"]
    faculties = ["Engineering", "Science", "Arts", "Social Sciences", "Business"]

    for _ in range(20):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        course = random.randint(1, 5)
        group_number = random.randint(100, 999)
        faculty_id = random.randint(1, 5)
        discipline_id = random.randint(1, len(subjects))
        query.exec(f'''
            INSERT INTO Students (first_name, last_name, course, discipline_id, faculty_id, group_number)
            VALUES ('{first_name}', '{last_name}', {course}, {discipline_id}, {faculty_id}, '{group_number}')
        ''')

    for subject in subjects:
        query.exec(f'''
            INSERT INTO Disciplines (subject)
            VALUES ('{subject}')
        ''')

    for faculty in faculties:
        query.exec(f'''
            INSERT INTO Faculties (faculty_name)
            VALUES ('{faculty}')
        ''')


# Создание триггеров
def createTriggers():
    query = QSqlQuery()
    query.exec('''
        CREATE TRIGGER IF NOT EXISTS check_student_input
        BEFORE INSERT ON Students
        FOR EACH ROW
        BEGIN
            IF NEW.course < 1 OR NEW.course > 5 THEN
                SELECT RAISE(ABORT, 'Course must be between 1 and 5');
            END IF;
        END;
    ''')
    query.exec('''
        CREATE TRIGGER IF NOT EXISTS delete_related_disciplines
        BEFORE DELETE ON Students
        FOR EACH ROW
        BEGIN
            DELETE FROM Disciplines WHERE id IN (
                SELECT discipline_id FROM Students WHERE id = OLD.id
            );
        END;
    ''')
    query.exec('''
            CREATE TRIGGER IF NOT EXISTS update_student_faculty
            AFTER UPDATE OF faculty_id ON Students
            FOR EACH ROW
            BEGIN
                UPDATE Students
                SET faculty_id = NEW.faculty_id
                WHERE faculty_id = OLD.faculty_id;
            END;
        ''')


if __name__ == '__main__':
    createConnection()
    createTablesAndData()
    createTriggers()