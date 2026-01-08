from flask import Flask, request
from src.db import *
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Universe'

@app.route('/tasks')
def get_tasks():
    connection = connect_to_database()
    list_of_tasks = read_from_database(connection, 'select * from tasks')
    disconnect_from_database(connection)
    return json.dumps(list_of_tasks, default=str)

@app.route('/tasks/task')
def get_task_by_id():
    id = request.args.get('id')
    if id:
        connection = connect_to_database()
        list_of_tasks = read_from_database(connection, f'select * from tasks where id = {id}')
        disconnect_from_database(connection)
        return json.dumps(list_of_tasks, default=str)
    
    category = request.args.get('category')
    if category:
        connection = connect_to_database()
        query = f'select * from tasks where category = "{category}"'
        list = read_from_database(connection, query)
        disconnect_from_database(connection)
        return json.dumps(list, default=str)
    
    return "No query parameter provided"

@app.route('/tasks/new/', methods=['POST'])
def add_new_task():

    task = request.json['task']
    category = request.json['category']
    due_date = request.json['due_date']
    done = request.json['done']
    
    connection = connect_to_database()
    query = f'insert into tasks (task, due_date, category, done) values ("{task}","{due_date}", "{category}", "{done}")'
    update_database(connection, query)
    disconnect_from_database(connection)
    
    return "success"

@app.route('/tasks/task', methods=['PUT'])
def update_task():
    id = request.args.get('id')
    
    task = request.json['task']
    category = request.json['category']
    due_date = request.json['due_date']
    done = request.json['done']
    
    connection = connect_to_database()
    query = f'update tasks set task = "{task}", category = "{category}", due_date = "{due_date}", done = "{done}" where id = {id}'
    update_database(connection, query)
    disconnect_from_database(connection)
    
    return "success"

@app.route('/tasks/task', methods=["DELETE"])
def delete_task():
    id = request.args.get('id')
    
    connection = connect_to_database()
    query = f'delete from tasks where id = {id}'
    update_database(connection, query)
    disconnect_from_database(connection)
    
    return "success"


if __name__ == '__main__':
    app.run()