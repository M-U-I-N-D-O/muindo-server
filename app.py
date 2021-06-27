from flask import Flask
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec
from view import look, mypage, auth, tinder, solution
from flask_marshmallow import Marshmallow
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_cors import CORS
from model import db

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    apispec = APISpec(
            title='MUINDO',
            version='v1',
            openapi_version='2.0',
            plugins=[MarshmallowPlugin()],
        )
    app.config.update({
        'APISPEC_SPEC': apispec
    })
    docs = FlaskApiSpec(app=app, document_options=False)

    with app.app_context():
        db.init_app(app)
        ma = Marshmallow(app)
    jwt = JWTManager(app)

    app.teardown_appcontext(shutdown_session)

    app.register_blueprint(look.looks)
    app.register_blueprint(mypage.mypage)
    app.register_blueprint(auth.auth)
    app.register_blueprint(tinder.tinder)
    app.register_blueprint(solution.solution)

    docs.register(look.get_musinsa_items, blueprint=look.looks.name)
    docs.register(look.upload_codi, blueprint=look.looks.name)
    docs.register(look.remove_look, blueprint=look.looks.name)

    docs.register(mypage.get_my_looks, blueprint=mypage.mypage.name)
    docs.register(mypage.get_my_look_detail, blueprint=mypage.mypage.name)
    docs.register(mypage.get_look_items_info, blueprint=mypage.mypage.name)
    docs.register(auth.get_access_token, blueprint=auth.auth.name)
    docs.register(auth.refresh, blueprint=auth.auth.name)
    docs.register(auth.get_access_token_for_guest, blueprint=auth.auth.name)

    docs.register(tinder.get_looks, blueprint=tinder.tinder.name)
    docs.register(tinder.confirm_look, blueprint=tinder.tinder.name)
    docs.register(tinder.thumbs_up, blueprint=tinder.tinder.name)
    docs.register(mypage.get_thumbs, blueprint=mypage.mypage.name)
    docs.register(tinder.cancle_thumbs_up, blueprint=tinder.tinder.name)
    docs.register(solution.get_sample_codis, blueprint=solution.solution.name)

    CORS(
            app,
            resources={
                r"*":{
                    "origins":["*"]
                    }
                },
            supports_credentials=True
    )

    from utils import error_handler_400
    from werkzeug.exceptions import BadRequest
    from marshmallow.exceptions import ValidationError
    app.register_error_handler(BadRequest, error_handler_400)
    #app.register_error_handler(ValidationError, error_handler_400)


    return app


def shutdown_session(response):
    db.session.remove()
    return response


app = create_app()

if __name__ == "__main__":
    app.run(threaded=True)
