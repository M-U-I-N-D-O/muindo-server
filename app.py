from flask import Flask
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec
from view import look, mypage
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='MUINDO',
            version='v1',
            openapi_version='2.0',
            plugins=[MarshmallowPlugin()],
        )
    })
    docs = FlaskApiSpec(app=app, document_options=False)

    with app.app_context():
        db = SQLAlchemy(app)
        ma = Marshmallow(app)
    jwt = JWTManager(app)

    app.register_blueprint(look.looks)
    app.register_blueprint(mypage.mypage)

    with app.app_context():
        docs.register(target=look.get_musinsa_items, blueprint=look.looks.name)
        docs.register(target=look.upload_codi, blueprint=look.looks.name)
        docs.register(target=look.confirm_codi, blueprint=look.looks.name)
        docs.register(target=mypage.get_looks, blueprint=mypage.mypage.name)

    return app


app = create_app()

if __name__ == "__main__":

    app.run()