

import json

def db_read():
    try:
        with open('todos.json', 'r') as f:
            data = json.load(f)
    except:
        data = {}
    return data

def db_write():
    with open('todos.json', 'w') as f:
        json.dump(todos, f)


todos=db_read()