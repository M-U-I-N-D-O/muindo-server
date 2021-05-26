from flask import Flask
from db import db
from flask_jwt_extended import JWTManager

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)

    jwt = JWTManager(app)

    from controller import closet

    app.register_blueprint(closet.closet)

    return app