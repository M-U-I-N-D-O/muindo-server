from flask import Flask
from model import db
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec
from view import closet


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)

    jwt = JWTManager(app)


    app.register_blueprint(closet.closet)
    docs = FlaskApiSpec(app)

    docs.register(closet.get_all_looks, blueprint=closet.closet.name)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()