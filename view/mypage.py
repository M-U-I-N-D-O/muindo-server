from flask import Blueprint, request, jsonify
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.look import *
from serializers.mypage import *
from service.mypage import *
from flask_jwt_extended import get_jwt
from decorators.view import auth_required

mypage = Blueprint("mypage", __name__, url_prefix="/mypage")


@mypage.errorhandler(422)
@mypage.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code



@mypage.route('/my-looks',methods=['GET'])
@auth_required(tags=['mypage'], description='내가 올린 룩들을 조회함.')
@marshal_with(LookSchema(many=True))
def get_my_looks():
    user_id=get_jwt()['sub']
    return MyPageService.get_my_looks(user_id)


@mypage.route('/my-looks/<int:look_id>', methods=['GET'])
@auth_required(tags=['mypage'], description='내가 올린 특정 룩의 각종 디테일한 사항들을 조회함')
@marshal_with(LookInfoDictSchema)
def get_my_look_detail(look_id):
    return MyPageService.get_my_look_detail(look_id)


@mypage.route('/my-looks/info', methods=['POST'])
@auth_required(tags=['mypage'], description='내가 올린 특정 룩의 각종 디테일한 사항들을 조회함')
@use_kwargs(GetItemInfoSchema)
@marshal_with(ItemsInfoSchema)
def get_look_items_info(**kwargs):
    items = GetItemInfoSchema().load(request.get_json())
    return MyPageService.get_items_info(items)


@mypage.route('/thumbs', methods=['GET'])
@auth_required(tags=['mypage'], description='내가 좋아요 누른 코디 목록 불러옴')
@use_kwargs({"lookid" : fields.String()}, location='query')
@marshal_with(LookSchema(many=True))
def get_thumbs(lookid=None):
    user_id=get_jwt()['sub']
    return MyPageService.get_my_thumbs(user_id, lookid)
