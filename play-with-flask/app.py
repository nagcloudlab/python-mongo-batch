from flask import Flask, render_template
from db import todos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        todos_count=len(todos),
        todos=todos
    )
    

@app.route('/todos/<int:todo_id>')
def todo_details(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    return render_template('todo.html', todo=todo)