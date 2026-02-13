from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from database import db
from models.project import Project
from schemas.project_schema import ProjectSchema

blp = Blueprint("projects", "projects", url_prefix="/api/v1/projects")


# ---------------- CREATE PROJECT ----------------
@blp.route("/", methods=["POST"])
@jwt_required()
@blp.arguments(ProjectSchema)
@blp.response(201, ProjectSchema)
def create_project(data):
    project = Project(**data)
    db.session.add(project)
    db.session.commit()
    return project


# ---------------- GET ALL PROJECTS ----------------
@blp.route("/", methods=["GET"])
@jwt_required()
@blp.response(200, ProjectSchema(many=True))
def get_projects():
    return Project.query.all()


# ---------------- GET SINGLE PROJECT ----------------
@blp.route("/<int:project_id>", methods=["GET"])
@jwt_required()
@blp.response(200, ProjectSchema)
def get_project(project_id):
    return Project.query.get_or_404(project_id)
