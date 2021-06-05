from flask import Blueprint
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.tinder import *
from service.tinder import *
from flask_jwt_extended import jwt_required, get_jwt


tinder = Blueprint("tinder", __name__, url_prefix="/tinder")


@doc(tags=['tinder'], description='무한적으로 넘기기')
@tinder.route('/tinder',methods=['GET'])
@jwt_required()
@marshal_with(TinderSchema(many=True))
def main_tinder():
    user_id = get_jwt()['sub']
    return TinderService.get_my_looks(user_id)


@doc(tags=['tinder'], description='테스트로 보내기')
@tinder.route('/test',methods=['GET'])
@marshal_with(TinderSchema(many=True))
def test_tinder():
    test =5
    return TinderService.get_test_looks(test)

