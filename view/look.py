from flask import Blueprint, request
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.look import LookRequest, MakeLookRequestSchema, ItemSchema, LookSchema
from service.look import ItemService, LookService
from flask_jwt_extended import jwt_required
looks = Blueprint("looks", __name__, url_prefix="/looks")


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items')
@use_kwargs(LookRequest, location="query")
@jwt_required()
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(middlecategory=None, subcategory=None, brand=None, type=None, itemid=None):
    return ItemService.get_musinsa_items(middlecategory, subcategory, brand, type, itemid)


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items/test')
@use_kwargs(LookRequest, location="query")
@marshal_with(ItemSchema(many=True))
def get_musinsa_items_dummy(middlecategory=None, subcategory=None, brand=None, type=None):
    return ItemService.get_musinsa_items(middlecategory, subcategory, brand, type)


@doc(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@looks.route('/upload', methods=['POST'])
@jwt_required()
@use_kwargs(MakeLookRequestSchema, location='form')
@marshal_with(LookSchema)
def upload_codi(items):

    print(items)

    return LookService.upload_look(request.json)


@doc(tags=['looks'], description='코디의 컨펌여부')
@looks.route('/confirm', methods=['POST', 'GET'])
def confirm_codi():
    return "코디의 컨펌여부"
