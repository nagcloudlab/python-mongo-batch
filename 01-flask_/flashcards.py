from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, abort
from model import data

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Welcome to my flashcards app!'

# @app.route('/date')
# def date():
#     return f'This page was served at {datetime.now()}'

# count=0
# @app.route('/count_views')
# def count_views():
#     global count
#     count += 1
#     return f'This page has been viewed {count} times!'

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', name='World', users=data, date=datetime.now())


@app.route('/users/<int:index>')
def users(index):
    try:
        user=data[index]
        return render_template('users.html', user=user,index=index,max_index=len(data)-1)
    except IndexError:
        # return render_template('404.html'), 404
        abort(404)