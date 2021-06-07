from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
from flask_apispec import doc, use_kwargs, marshal_with
from service.auth import *
from serializers.auth import *
from repository.auth import *

auth = Blueprint("auth", __name__, url_prefix="/auth")



@doc(tags=['auth'], description='어세스 토큰 쿠키에 담아서 보내기')
@auth.route('/access-token', methods=['POST'])
@use_kwargs(GetTokensRequestSchema)
@marshal_with(TokensSchema, code=201)
def get_access_token(email, name, uid, provider):
    if_first_time_insert_db(email, name, provider, uid)
    user_id = get_user_id(uid)
    return AuthService.create_tokens(user_id)


@doc(tags=['auth'], description='리프레시 토큰 발급')
@auth.route('/refresh3', methods=['GET'])
def hello():
    print(get_jwt()['sub'])
    return "hello"
