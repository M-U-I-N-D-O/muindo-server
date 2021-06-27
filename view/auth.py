from flask import Blueprint
from flask_jwt_extended import get_jwt,jwt_required
from flask_apispec import doc, use_kwargs, marshal_with
from service.auth import *
from serializers.auth import *
from repository.auth import *
from decorators.view import auth_required

import random
import string


auth = Blueprint("auth", __name__, url_prefix="/auth")

@doc(tags=['auth'], description='로그인')
@auth.route('/access-token', methods=['POST'])
@use_kwargs(GetTokensRequestSchema)
@marshal_with(TokensSchema, code=201)
def get_access_token(email, name, uid, provider):
    user_id=if_first_time_insert_db_and_get_user_id(email, name, provider, uid)
    return AuthService.create_tokens(user_id)


@auth.route('/refresh', methods=['POST'])
@auth_required(tags=['auth'], description='리프레시 토큰으로 어세스 토큰 재발급', refresh=True)
@marshal_with(AccessTokenSchema)
def refresh():
    user_id = get_jwt()['sub']
    return AuthService.create_access_token(user_id)


@doc(tags=['auth'], description='게스트 로그인')
@auth.route('/access-token-guest', methods=['GET'])
@marshal_with(TokensSchema, code=201)
def get_access_token_for_guest():
    uid = "".join([random.choice(string.ascii_letters) for _ in range(10)])
    user_id=guest_login("guset@guset.com", "guest", "guest", uid)
    return AuthService.create_tokens(user_id)
