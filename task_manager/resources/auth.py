from flask_smorest import Blueprint
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    verify_jwt_in_request
)
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from models.user import User
from schemas.user_schema import UserRegisterSchema, UserLoginSchema

blp = Blueprint("auth", "auth", url_prefix="/api/v1/auth")


# -------------------------
# REGISTER
# -------------------------
@blp.route("/register", methods=["POST"])
@blp.arguments(UserRegisterSchema)
def register(data):

    existing_users = User.query.count()

    # Case 1: First user must be admin
    if existing_users == 0:
        if data["role"] != "admin":
            return {"message": "First user must be an admin"}, 400

    # Case 2: After first admin exists → require admin token
    else:
        verify_jwt_in_request()

        current_user_id = get_jwt_identity()
        current_user = User.query.get(int(current_user_id))

        if not current_user:
            return {"message": "User not found"}, 404

        if current_user.role != "admin":
            return {"message": "Only admin can create users"}, 403

    user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data["role"],
        department_id=data.get("department_id")
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201


# -------------------------
# LOGIN
# -------------------------
@blp.route("/login", methods=["POST"])
@blp.arguments(UserLoginSchema)
def login(data):

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return {"message": "User not found"}, 404

    if not check_password_hash(user.password, data["password"]):
        return {"message": "Invalid credentials"}, 401

    access_token = create_access_token(
        identity=str(user.id),   # ✅ convert to string
        additional_claims={"role": user.role}
    )

    return {"access_token": access_token}, 200
