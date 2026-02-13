from flask import Flask
from flask_cors import CORS
from config import Config

from database import db
from extensions import jwt,api,limiter

from resources.auth import blp as AuthBlueprint
from resources.projects import blp as ProjectBlueprint
from resources.tasks import blp as TaskBlueprint
from resources.analytics import blp as AnalyticsBlueprint

def create_app():
    app=Flask(__name__)

    #load config
    app.config.from_object(Config)
    CORS(app)
    #initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    api.init_app(app)
    limiter.init_app(app)

    #register all blueprints
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(ProjectBlueprint)
    api.register_blueprint(TaskBlueprint)
    api.register_blueprint(AnalyticsBlueprint)

    return app
app=create_app()

with app.app_context():
    from models import user, department, project, task, comment, audit_log
    
    db.create_all()
if __name__=="__main__":
    app.run(debug=True)



