# encoding=utf-8
from flask import Flask, render_template, request
from config import config
from models import db
from helper import *


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task = request.form.get('task', None)
        change = request.form.get('change', None)
        if task:
            save(task)
        if change:
            update(change)
    todo_list, done_list = find()
    return render_template('index.html', todo_list=todo_list, done_list=done_list)


if __name__ == '__main__':
    app.run()
