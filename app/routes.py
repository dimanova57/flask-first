from app import app
from flask import render_template, redirect, request
import sqlite3

name = str()

def get_data():
    connection = sqlite3.connect("app/app.db")
    cursor = connection.cursor()
    cursor.execute("select name from groceries")
    all_data = cursor.fetchall()
    all_data = [i[0] for i in all_data]
    return all_data


def add_message(message):
    connection = sqlite3.connect("app/app.db")
    cursor = connection.cursor()
    cursor.execute("select name from groceries")
    cursor.execute("insert into groceries (name) values (?)", [message])
    connection.commit()
    connection.close()


@app.route('/')
def index():
    global name
    return render_template('main_page.html', all_data=get_data(), nickname=name)


@app.route('/messages', methods=['POST'])
def register():
    message = request.form['message']
    add_message(message)
    print(get_data())
    return redirect('/')


