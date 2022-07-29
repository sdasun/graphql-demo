# In a perfect world you would have
# authentication, a sperate resolver and a service for each bussiness logic,
# validations, database transactions, etc.
# Unfortunately we do not live in a perfect world

from task.models import SubTask, Task

def get(_, info, id):
    """Get a Task"""
    task = Task.objects.get(id=id)
    return {
        "task": task,
        "status": True
    }
def list(_, info):
    """Return List of Task"""
    tasks = Task.objects.all()
    return {
        "tasks": tasks,
        "status": True
    }


def create(_, info, title, description):
    """Create a Task"""
    task = Task.objects.create(title=title, description=description)
    return {
        "task": task,
        "status": True
    }


def create_complex(_, info, task):
    """Create a Task"""
    task = Task.objects.create(**task)
    return {
        "task": task,
        "status": True
    }


def mark_as_completed(_, info, id):
    """Mark a Task as completed"""
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()

    task.subtask_set.all().update(completed=True)
    return {
        "task": task,
        "status": True
    }


def update(_, info, id, title, description):
    """Update a Task"""
    task = Task.objects.get(id=id)
    task.title = title
    task.description = description
    task.save()
    return {
        "task": task,
        "status": True
    }


def delete(_, info, id):
    """Delete a Task"""
    task = Task.objects.get(id=id)
    task.delete()
    return {
        "status": True
    }


def subtask_by_task(task_obj, info):
    """Return List of SubTask"""
    return task_obj.subtask_set.all()
