from flask import Flask
from model import db
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec
from view import look, mypage, auth


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(look.looks)
    app.register_blueprint(mypage.mypage)
    app.register_blueprint(auth.auth)


    docs = FlaskApiSpec(app)
    docs.register(look.get_musinsa_items, blueprint=look.looks.name)
    docs.register(look.upload_codi, blueprint=look.looks.name)
    docs.register(look.confirm_codi, blueprint=look.looks.name)
    docs.register(mypage.get_looks, blueprint=mypage.mypage.name)
    docs.register(auth.get_access_token, blueprint=auth.auth.name)
    docs.register(auth.refresh, blueprint=auth.auth.name)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)