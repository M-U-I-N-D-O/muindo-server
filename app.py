<<<<<<< HEAD
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec
from view import look, mypage, auth, tinder
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_cors import CORS


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

    app.teardown_appcontext(shutdown_session)

    app.register_blueprint(look.looks)
    app.register_blueprint(mypage.mypage)
    app.register_blueprint(auth.auth)
    app.register_blueprint(tinder.tinder)

    docs.register(look.get_musinsa_items, blueprint=look.looks.name)
    docs.register(look.upload_codi, blueprint=look.looks.name)
    docs.register(look.confirm_codi, blueprint=look.looks.name)
    docs.register(mypage.get_my_looks, blueprint=mypage.mypage.name)
    docs.register(mypage.get_my_look_detail, blueprint=mypage.mypage.name)
    docs.register(auth.get_access_token, blueprint=auth.auth.name)
    docs.register(auth.refresh, blueprint=auth.auth.name)
    docs.register(tinder.main_tinder, blueprint=tinder.tinder.name)
    docs.register(tinder.test_tinder, blueprint=tinder.tinder.name)

    CORS(
            app,
            resources={
                r"*":{
                    "origins":["*"]
                    }
                }
    )

    return app

def shutdown_session(response):

    from model import db
    db.session.remove()
    return response

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec
from view import look, mypage, auth, tinder
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_cors import CORS


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

    app.teardown_appcontext(shutdown_session)

    app.register_blueprint(look.looks)
    app.register_blueprint(mypage.mypage)
    app.register_blueprint(auth.auth)
    app.register_blueprint(tinder.tinder)

    docs.register(look.get_musinsa_items, blueprint=look.looks.name)
    docs.register(look.upload_codi, blueprint=look.looks.name)
    docs.register(look.confirm_codi, blueprint=look.looks.name)
    docs.register(mypage.get_my_looks, blueprint=mypage.mypage.name)
    docs.register(mypage.get_my_look_detail, blueprint=mypage.mypage.name)
    docs.register(mypage.get_look_items_info, blueprint=mypage.mypage.name)
    docs.register(auth.get_access_token, blueprint=auth.auth.name)
    docs.register(auth.refresh, blueprint=auth.auth.name)
    docs.register(tinder.main_tinder, blueprint=tinder.tinder.name)
    docs.register(tinder.test_tinder, blueprint=tinder.tinder.name)

    CORS(
            app,
            resources={
                r"*":{
                    "origins":["*"]
                    }
                }
    )

    return app

def shutdown_session(response):

    from model import db
    db.session.remove()
    return response

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> b70d536ba1fe58691ba3d79aaab3167490b2a8d0
