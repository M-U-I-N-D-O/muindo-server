from flask import  jsonify, Blueprint, Response
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt_request_location,get_jwt

from flask_apispec import doc, use_kwargs, marshal_with
from service.auth import *
from serializers.auth import *
from repository.auth import *

auth = Blueprint("auth", __name__, url_prefix="/auth")



@doc(tags=['auth'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@auth.route('/access-token', methods=['POST'])
@use_kwargs(GetTokensRequestSchema)
@marshal_with(TokensSchema, code=201)
def get_access_token(email, name, uid, provider):
    if_first_time_insert_db(email, name, provider, uid)
    user_id = get_user_id(uid)
    return AuthService.create_tokens(user_id)



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
