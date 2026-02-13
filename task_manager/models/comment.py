from database import db
from datetime import datetime

class Comment(db.Model):
    __tablename__="comments"

    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.Text,nullable=False)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)

    task_id=db.Column(db.Integer,db.ForeignKey("tasks.id"),nullable=False)

    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)

    #many comments fro one task
    task=db.relationship("Task",back_populates="comments")

    #many comments from one user

    user=db.relationship("User",back_populates="comments")

    
