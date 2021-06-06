from flask import Blueprint
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.mypage import *
from service.mypage import *
from flask_jwt_extended import jwt_required, get_jwt


mypage = Blueprint("mypage", __name__, url_prefix="/mypage")

@doc(tags=['mypage'], description='내가 올린 룩들을 조회함.')
@mypage.route('/my-looks',methods=['GET'])
@jwt_required()
@marshal_with(MyLooksSchema(many=True))
def get_my_looks():
    user_id=get_jwt()['sub']
    return MyPageService.get_my_looks(user_id)


@doc(tags=['mypage'], description='내가 올린 특정 룩의 각종 디테일한 사항들을 조회함')
@mypage.route('/my-looks/<int:look_id>', methods=['GET'])
@jwt_required()
@marshal_with(MyLooksSchema)
def get_my_look_detail(look_id):
    return MyPageService.get_my_look_detail(look_id)


@doc(tags=['mypage'], description='내가 올린 특정 룩의 각종 디테일한 사항들을 조회함')
@mypage.route('/my-looks/info', methods=['GET'])
@use_kwargs(GetItemInfoSchema)
@jwt_required()
@marshal_with(ItemsInfoSchema(many=True))
def get_look_items_info(hat_id, top_id, bottom_id, shoes_id, bag_id ):
    return MyPageService.get_items_info(hat_id, top_id, bottom_id, shoes_id, bag_id)