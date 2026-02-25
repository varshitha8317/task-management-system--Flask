import os
from datetime import timedelta
class Config:

    #basic flask config
    SECRET_KEY=os.getenv("SECRET_KEY","dev-secret-key")
    DEBUG=True

    #database config

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    #jwt authentication config

    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY","jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=7)
    JWT_TOKEN_LOCATION=["headers"]
    JWT_HEADER_NAME="Authorization"
    JWT_HEADER_TYPE="Bearer"

    #flask smorest /swagger config

    API_TITLE="Advanced Task Management API"
    API_VERSION="v1"
    OPENAPI_VERSION="3.0.3"
    OPENAPI_URL_PREFIX="/"
    OPENAPI_SWAGGER_UI_PATH="/swagger"
    OPENAPI_SWAGGER_UI_URL="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    #rate timing config
    RATELIMIT_HEADERS_ENABLED=True
    RATELIMIT_DEFAULT="200 per day;50 per hour"

    # celery + redis config(background jobs)

    CELERY_BROKER_URL=os.getenv("CELERY_BROKER_UR","redis://localhost:6379/0")
    CELERY_RESULT_BACKEND=os.getenv("CELERY_RESULT_BACKEND","redis://localhost:6379/0")

    #email config
    MAIL_SERVER="smtp.gmail.com"
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER=MAIL_USERNAME

    # socket .io (real time updates
    
    SOCKETIO_MESSAGE_QUEUE=os.getenv("SOCKETIO_MESSAGE_QUEUE","redis://localhost:6379/1")

    ENABLE_ANALYTICS=True