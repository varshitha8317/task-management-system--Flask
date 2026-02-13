from database import db

class Project(db.Model):
    __tablename__="projects"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)

    #one project can have many tasks

    tasks=db.relationship("Task",back_populates="project",lazy=True)