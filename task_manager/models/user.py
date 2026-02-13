from database import db

class User(db.Model):
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)
    role=db.Column(db.String(20))

    department_id=db.Column(db.Integer,db.ForeignKey("departments.id"),nullable=True)

    #many users are from one department
    department=db.relationship("Department",back_populates="users")

    #one user can have many comments 
    comments=db.relationship("Comment",back_populates="user",lazy=True)
