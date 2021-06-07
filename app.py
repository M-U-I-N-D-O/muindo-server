from datetime import datetime
from datetime import timedelta
from datetime import timezone
from flask import Flask
from flask_jwt_extended import JWTManager, get_jwt, create_access_token,set_access_cookies
from flask_apispec import FlaskApiSpec
from view import look, mypage, auth, tinder
from flask_marshmallow import Marshmallow
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_cors import CORS
from model import db

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
        db.init_app(app)
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
    docs.register(tinder.get_looks, blueprint=tinder.tinder.name)
    docs.register(tinder.confirm_look, blueprint=tinder.tinder.name)

    CORS(
            app,
            resources={
                r"*":{
                    "origins":["*"]
                    }
                }
    )

    from utils import error_handler_400
    from werkzeug.exceptions import BadRequest
    from marshmallow.exceptions import ValidationError
    app.register_error_handler(BadRequest, error_handler_400)
    app.register_error_handler(ValidationError, error_handler_400)
    app.register_error_handler(422, error_handler_400)

    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt()['sub'])
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response

    return app


def shutdown_session(response):
    db.session.remove()
    return response


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
