from flask import Blueprint,request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
from flask_apispec import doc, use_kwargs, marshal_with
from service.auth import *
from serializers.auth import *
from repository.auth import *
from decorators.view import auth_required

import random
import string


auth = Blueprint("auth", __name__, url_prefix="/auth")



@auth_required(tags=['auth'], description='로그인')
@auth.route('/access-token', methods=['POST'])
@use_kwargs(GetTokensRequestSchema)
@marshal_with(TokensSchema, code=201)
def get_access_token(email, name, uid, provider):
    if_first_time_insert_db(email, name, provider, uid)
    user_id = get_user_id(uid)
    return AuthService.create_tokens(user_id)



@auth_required(tags=['auth'], description='리프레시 토큰으로 어세스 토큰 재발급', refresh=True)
@auth.route('/refresh', methods=['POST'])
@marshal_with(AccessTokenSchema)
def refresh():
    user_id = get_jwt()['sub']
    return AuthService.create_access_token(user_id)


@doc(tags=['auth'], description='로그인')
@auth.route('/access-token-guest', methods=['GET'])
@marshal_with(TokensSchema, code=201)
def get_access_token_for_guest():
    uid = "".join([random.choice(string.ascii_letters) for _ in range(10)])
    if_first_time_insert_db("guset@guset.com", "guest", "guest", uid)
    user_id = get_user_id(uid)
    return AuthService.create_tokens(user_id)
