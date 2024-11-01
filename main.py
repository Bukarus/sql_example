import sqlite3
import os

with sqlite3.connect(os.path.join('C:\\Users\\User\\', 'database.db')) as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, surname) VALUES ('Иван', 'Иванов');")
    # cursor.execute("INSERT INTO students (name, surname) VALUES ('Петр', 'Петров');")
    # cursor.execute("INSERT INTO students (name, surname) VALUES ('Анна', 'Аннова');")

    cursor.execute("SELECT * FROM students;")
    print(cursor.fetchall())
    conn.commit()
