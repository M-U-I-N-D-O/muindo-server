from flask import Blueprint
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import fields
from serializers.look import LookSchema
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
@tinder.route('/confirm', methods=['GET'])
@use_kwargs({'itemid': fields.Integer()}, location="query")
@jwt_required()
@marshal_with(LookSchema(many=True))
def main_tinder(itemid=None):
    user_id = get_jwt()['sub']
    return TinderService.get_random_looks(user_id, itemid)


@doc(tags=['tinder'], description='테스트로 보내기')
@tinder.route('/test',methods=['GET'])
@marshal_with(LookSchema(many=True))
def test_tinder():
    test =5
    return TinderService.get_test_looks(test)

