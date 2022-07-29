# In a perfect world, You would have 
# authentication, a sperate resolver and a service for each bussiness logic, 
# validations, database transactions & etc.
# Unfortunately, We are not living in a perfect world.

from ariadne import convert_kwargs_to_snake_case
from task.models import SubTask, Task

@convert_kwargs_to_snake_case
def create(_, info, task_id, title, description):
    """Create a SubTask"""
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return {"error": "Task does not exist"}
    subtask = SubTask.objects.create(task=task, title=title, description=description)
    return {
        "subTask": subtask,
    }

def mark_as_completed(_, info, id):
    """Mark a SubTask as completed"""
    subtask = SubTask.objects.get(id=id)
    subtask.completed = True
    subtask.save()
    return {
        "subTask": subtask,
        "status": True
    }

def update(_, info, id, title, description):
    """Update a SubTask"""
    subtask = SubTask.objects.get(id=id)
    subtask.title = title
    subtask.description = description
    subtask.save()
    return {
        "subTask": subtask,
        "status": True
    }

def delete(_, info, id):
    """Delete a SubTask"""
    subtask = SubTask.objects.get(id=id)
    subtask.delete()
    return {
        "status": True
    }

def get(_, info, id):
    """Get a SubTask"""
    sub_task = SubTask.objects.get(id=id)
    return {
        "subTask": sub_task,
        "status": True
    }
    
def task_by_subtask(subtask_obj, info):
    """Return Task"""
    return subtask_obj.task