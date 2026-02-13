from database import db

class Department(db.Model):
    __tablename__="departments"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)

    #one department can have many users
    users=db.relationship("User",back_populates="department",lazy=True)