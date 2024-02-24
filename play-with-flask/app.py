from flask import Flask, render_template,request,redirect,abort,url_for
from db import todos, db_write

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        todos_count=len(todos),
        todos=todos
    )

@app.route('/add_todo', methods=['GET', 'POST'])
def handle_new_todo():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        todos.append({
            'id': len(todos) + 1,
            'title': title,
            'description': description
        })
        db_write()
        # return redirect(f'/todos/{len(todos) - 1}')
        return redirect(url_for('todo_details', todo_id=len(todos)))
    else:
        return render_template(
            'add_todo.html'
        )
        

@app.route('/todos/<int:todo_id>')
def todo_details(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        return render_template('not_found.html')
        # abort(404)
    return render_template('todo.html', todo=todo, max_id=len(todos))