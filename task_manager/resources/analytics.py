from flask_smorest import Blueprint
from models.task import Task
from datetime import date

blp=Blueprint("analytics","analytics",url_prefix="/api/v1/analytics")

@blp.route("/status",methods=["Get"])
def status():
    return {
        "total_tasks":Task.query.count(),
        "completed_tasks":Task.query.filter_by(status="completed").count(),
        "overdue_tasks":Task.query.filter(Task.due_date<date.today()).count()
    }
