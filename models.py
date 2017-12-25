# encoding=utf-8

from flask_mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()


class Task(db.Document):
    meta = {
        'collection': 'tasks',
        'ordering': ['-create_at'],
        'strict': False
    }
    name = db.StringField()
    create_at = db.DateTimeField(default=datetime.now)
    is_completed = db.BooleanField(default=False)
