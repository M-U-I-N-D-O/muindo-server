from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from controller.auth import Login, Refresh
from flasgger import Swagger

from app import config

def create_app():

    app = Flask(__name__)
    api = Api(app)
    swagger = Swagger(app)

    app.config.from_object(config)
    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)
    api.add_resource(Login, '/auth/login')
    api.add_resource(Refresh, '/auth/refresh')

    return app