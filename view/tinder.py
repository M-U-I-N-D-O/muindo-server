from flask import Blueprint, request
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import fields
from serializers.look import LookSchema
from serializers.tinder import ConfirmSchema
from service.tinder import *
from flask_jwt_extended import jwt_required, get_jwt


tinder = Blueprint("tinder", __name__, url_prefix="/tinder")


@doc(tags=['tinder'], description='컨펌 받기 위한 코디 이미지 불러오기')
@doc(
    description='need access-token',
    params={
        'Authorization': {
            'description':
            'Authorization HTTP header with JWT access token, like: Authorization: Bearer asdf.qwer.zxcv',
            'in': 'header',
            'type':'string',
            'required': True
        }
    })
@tinder.route('/look', methods=['GET'])
@use_kwargs({'itemid': fields.Integer()}, location="query")
@jwt_required()
@marshal_with(LookSchema(many=True))
def get_looks(itemid=None):
    user_id = get_jwt()['sub']
    return TinderService.get_random_looks(user_id, itemid)


@doc(tags=['tinder'], description='코디 컨펌하기')
@tinder.route('/confirm', methods=['POST'])
@use_kwargs(ConfirmSchema)
def confirm_look(**kwargs):

    confirm = ConfirmSchema().load(request.get_json())
    body = {}
    code = None

    if TinderService.confirm_looks(confirm):

        body['message'] = '컨펌되었습니다.'
        code = 201

    else:
        body['message'] = '컨펌 실패'
        code = 200

    from flask import jsonify

    return jsonify(body), code
