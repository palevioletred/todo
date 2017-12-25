# encoding=utf-8
from models import Task


def save(task_name):
    task = Task(name=task_name, is_completed=False)
    task.save()


def find():
    todo_list = []
    done_list = []
    tasks = Task.objects().all()
    for task in tasks:
        name = task.name
        is_completed = task.is_completed
        create_at = task.create_at
        if not is_completed:
            todo_list.append({'name': name, 'create_at': create_at})
            continue
        done_list.append({'name': name, 'create_at': create_at})
    return todo_list, done_list


def delete(task_name, create_at):
    task = Task.objects(name=task_name, create_at=create_at).first()
    if task:
        task.delete()


def update(task_name):
    tasks = Task.objects(name=task_name).all()
    for task in tasks:
        task.update(is_completed=not task.is_completed)
