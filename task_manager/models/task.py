from database import db
from datetime import date

# Association table for many to many task and user

task_assignments=db.Table("task_assignments",
db.Column("task_id",db.Integer,db.ForeignKey("tasks.id")),
db.Column("user_id",db.Integer,db.ForeignKey("users.id"))
)


class Task(db.Model):
    __tablename__="tasks"

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    description=db.Column(db.Text)
    priority=db.Column(db.String(20))
    status=db.Column(db.String(20),default="Pending")
    due_date=db.Column(db.Date)

    project_id=db.Column(db.ForeignKey("projects.id"),nullable=False)
   # mnay tasks are related to one project
    project=db.relationship("Project",back_populates="tasks")

    #many tasks with many users

    assigned_users=db.relationship("User",secondary=task_assignments,backref="tasks")
    

    # one task can have many comments
    comments=db.relationship("Comment",back_populates="task",lazy=True)
