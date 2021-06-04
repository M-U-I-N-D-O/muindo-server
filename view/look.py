from flask import Blueprint, request
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.look import LookRequest, ItemResponseShcema, ItemSchema
from service.look import ItemService, LookService

looks = Blueprint("looks", __name__, url_prefix="/looks")


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items')
@use_kwargs(LookRequest, location="query")
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(middlecategory=None, subcategory=None, brand=None, type=None):
    return ItemService.get_musinsa_items(middlecategory, subcategory, brand, type)


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items/test')
@use_kwargs(LookRequest, location="query")
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(middlecategory=None, subcategory=None, brand=None, type=None):
    return ItemService.get_musinsa_items(middlecategory, subcategory, brand, type)


@doc(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@looks.route('/upload', methods=['POST'])
def upload_codi():

    img = request.json
    print(img.items())

    return LookService.upload_look_azure(request.json.get('data').get('img'))


@doc(tags=['looks'], description='코디의 컨펌여부')
@looks.route('/confirm', methods=['POST', 'GET'])
def confirm_codi():

    import requests

    response = requests.get('https://sherlockodds.blob.core.windows.net/musinsa/1159STUDIO_1477298_1_500.jpg')

    if response.status_code == 200:
        print(response.headers.get('Access-Control-Allow-Origin'))
    return "코디의 컨펌여부"
