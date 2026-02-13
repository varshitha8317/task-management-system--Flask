from flask_jwt_extended import JWTManager
from flask_smorest import Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

jwt=JWTManager()
api=Api()
limiter=Limiter(key_func=get_remote_address)