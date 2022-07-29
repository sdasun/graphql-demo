from ariadne import (
    MutationType,
    ObjectType,
    QueryType,
    load_schema_from_path,
    make_executable_schema
)
from task.bussiness import (
    task as task_resolver,
    subtask as subtask_resolver,
)

# Query
query = QueryType()
query.set_field("tasks", task_resolver.list)
query.set_field("task", task_resolver.get)
 
# Object Type
task = ObjectType("Task")
task.set_field("subTasks", task_resolver.subtask_by_task)

sub_task = ObjectType("SubTask")
sub_task.set_field("task", subtask_resolver.task_by_subtask)

# Mutation
mutation = MutationType()
mutation.set_field("createTask", task_resolver.create)
mutation.set_field("createTaskComplex", task_resolver.create_complex)
mutation.set_field("markTaskAsCompleted", task_resolver.mark_as_completed)
mutation.set_field("createSubTask", subtask_resolver.create)
mutation.set_field("markSubTaskAsCompleted", subtask_resolver.mark_as_completed)

type_def_list = [
    load_schema_from_path("task/apis/schema/query.graphql"),
    load_schema_from_path("task/apis/schema/mutation.graphql"),
]

schema = make_executable_schema(
    type_def_list,
    query,
    mutation,
    task,
    sub_task
)
