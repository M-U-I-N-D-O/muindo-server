from flask import  jsonify, Blueprint, Response
from flask_restful import wraps
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token

from flask_apispec import doc
from service.auth import if_first_time_insert_db, create_tokens
from serializers.auth import *
from marshmallow import ValidationError

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
def get_access_token() -> Response:
    data=request.get_json()
    try:
        email, name, provider, unique_id = deserialize_request(data)
    except ValidationError as err:
        return err.messages, 400
    if_first_time_insert_db(email, name, provider, unique_id)
    access_token, refresh_token = create_tokens(unique_id)
    serialized_tokens = SerializeTokens(access_token, refresh_token)
    return Response(serialized_tokens,200)


@doc(tags=['auth'], description='리프레시 토큰 발급')
@auth.route('/refresh-token', methods=['POST'])
@jwt_required(refresh=True)
def refresh() -> Response:
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return Response(access_token, 200)

