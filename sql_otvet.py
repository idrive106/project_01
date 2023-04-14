import sqlite3

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL, 
School_ID INTEGER NOT NULL
);
"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_ID) 
VALUES 
('201', 'Иван', 1), 
('202', 'Петр', 2), 
('203', 'Анастасия', 3), 
('204', 'Игорь', 4);
"""
cursor.execute(query)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_info(student_id):
    try:
     connection = sqlite3.connect('teachers.db')
     cursor = connection.cursor()
     sql_select_query = """
     SELECT Students.student_Id, Students.student_name, Students.school_id, School.School_name
     FROM Students
     JOIN School ON Students.school_id = School.School_id
     WHERE Students.student_Id = ?
     """
     cursor.execute(sql_select_query, (student_id,))
     student_data = cursor.fetchone()
     print("ID студента:", student_data[0])
     print("Имя студента:", student_data[1])
     print("ID школы:", student_data[2])
     print("Название школы:", student_data[3])
     connection.close()
    except (Exception, sqlite3.Error) as error:
      print("Ошибка в получении данных", error)

get_student_info(201)

