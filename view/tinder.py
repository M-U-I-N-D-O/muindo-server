from flask import Blueprint, request
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import fields
from serializers.look import LookSchema
from serializers.tinder import ConfirmSchema
from service.tinder import *
from flask_jwt_extended import jwt_required, get_jwt
from utils import userid


tinder = Blueprint("tinder", __name__, url_prefix="/tinder")


@doc(tags=['tinder'], description='컨펌 받기 위한 코디 이미지 불러오기')
@tinder.route('/look', methods=['GET'])
@use_kwargs({'itemid': fields.Integer()}, location="query")
@marshal_with(LookSchema(many=True))
def get_looks(itemid=None):
    user_id = userid
    return TinderService.get_random_looks(user_id, itemid)


@doc(tags=['tinder'], description='코디 컨펌하기')
@tinder.route('/confirm', methods=['POST'])
@use_kwargs(ConfirmSchema)
def confirm_look(**kwargs):

    confirm = ConfirmSchema().load(request.get_json())
    return TinderService.confirm_looks(confirm)

