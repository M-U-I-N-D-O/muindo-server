from flask import  jsonify, Blueprint, Response
from flask_restful import wraps
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt_request_location,get_jwt

from flask_apispec import doc, use_kwargs, marshal_with
from service.auth import *
from serializers.auth import *

auth = Blueprint("auth", __name__, url_prefix="/auth")


def access_token_required(f):
    f.__access_token_required = True
    @wraps(f)
    def decorated(*args, **kwargs):
        print('do_something_with_access_token')

        return f(*args, **kwargs)

    return decorated


@doc(tags=['auth'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@auth.route('/access-token', methods=['POST'])
@use_kwargs(GetTokensRequestSchema)
@marshal_with(TokensSchema, code=201)
def get_access_token(email, name, uid, provider):
    if_first_time_insert_db(email, name, provider, uid)
    print(uid)
    return AuthService.create_tokens(uid)



@doc(tags=['auth'], description='리프레시 토큰 발급')
@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
@marshal_with(AccessTokenSchema)
def refresh():
    uid=get_jwt()['sub']
    return AuthService.create_access_token(uid)




@doc(tags=['auth'], description='리프레시 토큰 발급')
@auth.route('/refresh3', methods=['GET'])
@jwt_required()
def hello():
    print(get_jwt()['sub'])
    return "hello"
