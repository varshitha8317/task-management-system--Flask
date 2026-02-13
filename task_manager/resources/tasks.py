from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.task import Task
from models.user import User
from schemas.task_schema import TaskCreateSchema, TaskUpdateSchema

blp = Blueprint("tasks", "tasks", url_prefix="/api/v1/tasks")


# ---------------------------------------------------
# CREATE TASK (Only Manager)
# ---------------------------------------------------
@blp.route("/", methods=["POST"])
@jwt_required()
@blp.arguments(TaskCreateSchema)
def create_task(data):

    current_user_id = get_jwt_identity()
    current_user = User.query.get(int(current_user_id))

    if current_user.role != "manager":
        return {"message": "Only managers can create tasks"}, 403

    task = Task(
        title=data["title"],
        description=data.get("description"),
        priority=data.get("priority"),
        due_date=data.get("due_date"),
        project_id=data.get("project_id")
    )

    # Assign only employees
    if data.get("assigned_user_ids"):
        users = User.query.filter(
            User.id.in_(data["assigned_user_ids"]),
            User.role == "employee"
        ).all()

        task.assigned_users = users

    db.session.add(task)
    db.session.commit()

    return {"message": "Task created successfully"}, 201


# ---------------------------------------------------
# UPDATE TASK (Only Manager)
# ---------------------------------------------------
@blp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
@blp.arguments(TaskUpdateSchema)
def update_task(data, task_id):

    current_user_id = get_jwt_identity()
    current_user = User.query.get(int(current_user_id))

    if current_user.role != "manager":
        return {"message": "Only managers can update tasks"}, 403

    task = Task.query.get_or_404(task_id)

    if "title" in data:
        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    if "priority" in data:
        task.priority = data["priority"]

    if "status" in data:
        task.status = data["status"]

    db.session.commit()

    return {"message": "Task updated successfully"}, 200


# ---------------------------------------------------
# GET ALL TASKS
# ---------------------------------------------------
@blp.route("/", methods=["GET"])
@jwt_required()
def get_tasks():

    tasks = Task.query.all()

    return [
        {
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "status": t.status
        }
        for t in tasks
    ], 200


# ---------------------------------------------------
# DELETE TASK (Only Manager)
# ---------------------------------------------------
@blp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):

    current_user_id = get_jwt_identity()
    current_user = User.query.get(int(current_user_id))

    if current_user.role != "manager":
        return {"message": "Only managers can delete tasks"}, 403

    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return {"message": "Task deleted successfully"}, 200
