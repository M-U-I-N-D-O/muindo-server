from flask import Blueprint, request, Response
from flask_apispec import use_kwargs, marshal_with
from marshmallow import fields
from serializers.look import LookSchema
from serializers.tinder import ConfirmSchema, UpdateThumb
from service.tinder import *
from flask_jwt_extended import get_jwt
from decorators.view import auth_required

tinder = Blueprint("tinder", __name__, url_prefix="/tinder")

@tinder.route('/look', methods=['GET'])
@auth_required(tags=['tinder'], description='컨펌 받기 위한 코디 이미지 불러오기')
@use_kwargs({'itemid': fields.Integer()}, location="query")
@marshal_with(LookSchema(many=True))
def get_looks(itemid=None):
    user_id = get_jwt()['sub']
    return TinderService.get_random_looks(user_id, itemid)


@tinder.route('/confirm', methods=['POST'])
@auth_required(tags=['tinder'], description='코디 컨펌하기')
@use_kwargs(ConfirmSchema)
def confirm_look(**kwargs):
    confirm = ConfirmSchema().load(request.get_json())
    confirm['userid'] = get_jwt()['sub']
    return TinderService.confirm_looks(confirm)


@tinder.route('/thumbs/<int:lookid>', methods=['PUT'])
@auth_required(tags=['tinder'], description='좋아요')
@use_kwargs(UpdateThumb)
def thumbs_up(lookid, **kwargs):

    update_thumb = UpdateThumb()
    data = update_thumb.load(kwargs)
    data['userid'] = get_jwt()['sub']
    data['lookid'] = lookid
    code = TinderService.add_thumbs_up(data)

    if code :
        return Response(status=201)

    return Response()

@tinder.route('/thumbs/<int:lookid>', methods=['DELETE'])
@auth_required(tags=['tinder'], description='좋아요 취소')
def cancle_thumbs_up(lookid):
    TinderService.remove_thumb(get_jwt()['sub'], lookid)
    return Response(status=200)
