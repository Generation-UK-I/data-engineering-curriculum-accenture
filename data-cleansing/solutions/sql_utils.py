import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

def setup_db_connection(host=host_name,
                        user=user_name,
                        password=user_password,
                        db=database_name):

    connection = pymysql.connect(
        host = host,
        database = db,
        user = user,
        password = password
    )
    return connection

def create_db_tables(connection):
    create_student_data_table = """
        CREATE TABLE IF NOT EXISTS students (
            id INT NOT NULL,
            name VARCHAR(50),
            age INT,
            branch VARCHAR(50),
            start_date DATE,
            teacher VARCHAR(50),
            tel VARCHAR(20),
            PRIMARY KEY (id)
        );
    """

    cursor = connection.cursor()
    cursor.execute(create_student_data_table)
    connection.commit()
    cursor.close()


def insert_students(connection, student_list):
    sql = """
        INSERT INTO students (id, name, age, branch, teacher, start_date, tel)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    cursor = connection.cursor()
    for student in student_list:
        row = (student['id'], student['name'],
            student['age'], student['branch'],
            student['teacher'], student['start_date'],
            student['tel'])
        cursor.execute(sql, row)

    connection.commit()
    cursor.close()
    print('Rows inserted.')
