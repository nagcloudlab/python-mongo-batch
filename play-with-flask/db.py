

import json

def db_read():
    try:
        with open('todos.json', 'r') as f:
            data = json.load(f)
    except:
        data = {}
    return data


todos=db_read()