import pymysql
from dotenv import load_dotenv
import os

def connect_to_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    return pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=database
    )

def disconnect_from_database(connection):
    connection.close()

def read_from_database(connection, query):
    list_from_database = []
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for row in rows:
        forming_dict = {}
        j = 0
        for x in row:
            forming_dict[field_names[j]] = x
            j += 1
        list_from_database.append(forming_dict)
    cursor.close()
    connection.commit()
    return list_from_database 

def update_database(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    connection.commit()