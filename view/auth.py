from flask import  jsonify, request, Flask, redirect, session
from flask_restful import  Resource, Api
from flask_restful import wraps
# flask_jwt_extended를 사용하여 서버와 클라이언트 사이에서 토큰으로 인증
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

def access_token_required(f):
    f.__access_token_required = True

    @wraps(f)
    def decorated(*args, **kwargs):
        print('do_something_with_access_token')

        return f(*args, **kwargs)

    return decorated
class Login(Resource):
    def post(self):
        """
        This examples uses FlaskRESTful Resource
        It works also with swag_from, schemas and spec_dict
        ---
        parameters:
          - in: body
            name: uid
            type: object
            required: true
        responses:
          200:
            description: login
            schema:
              id: User
              properties:
                access_token:
                  type: string
                  description: access_token for maintain login status
                  default: default
                  """
        unique_id = request.json.get('uid')
        access_token = create_access_token(identity=unique_id, fresh= True)
        refresh_token = create_refresh_token(identity=unique_id)

        return jsonify(access_token=access_token, refresh_token=refresh_token)


class Refresh(Resource):
    def post(self):
        """
        parameters:
          - in: body
            name: refresh_token
            type: object
            required: true
        responses:
          200:
            description: refresh
            schema:
              id: User
              properties:
                access_token:
                  type: string
                  description: access_token for maintain login status
                  default: default
                  """
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        return jsonify(access_token=access_token)