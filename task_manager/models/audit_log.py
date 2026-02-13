from database import db
from datetime import datetime

class AuditLog(db.Model):
    __tablename__="audit_logs"
    id=db.Column(db.Integer,primary_key=True)
    action=db.Column(db.String(200),nullable=False)

    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)

    timestamp=db.Column(db.DateTime,default=datetime.utcnow)

    #many logs one user
    user=db.relationship("User")