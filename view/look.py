from flask import Blueprint
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.look import LookRequest, ItemSchema
from service.look import ItemService
looks = Blueprint("looks", __name__, url_prefix="/looks")


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items')
@use_kwargs(LookRequest, location="query")
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(**kwargs):
    return ItemService.get_musinsa_items(kwargs)



@doc(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@looks.route('/upload', methods=['POST'])
def upload_codi():

    return "조합한 아이템들을 코디로 만듬"


@doc(tags=['looks'],description='코디의 컨펌여부')
@looks.route('/confirm', methods=['POST'])
def confirm_codi():

    return "코디의 컨펌여부"




