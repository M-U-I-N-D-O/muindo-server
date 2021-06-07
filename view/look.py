from flask import Blueprint, request
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.look import LookRequest, LookSchema, ItemSchema, MakeLookRequest
from service.look import ItemService, LookService
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
looks = Blueprint("looks", __name__, url_prefix="/looks")


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items')
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(middlecategory=None, subcategory=None, brand=None, type=None, itemid=None):
    return ItemService.get_musinsa_items(middlecategory, subcategory, brand, type, itemid)


@doc(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@looks.route('/upload', methods=['POST'])
@marshal_with(LookSchema)
def upload_codi():

    schema = MakeLookRequest()
    try:
        newlook = schema.load(request.get_json())

    except ValidationError as error:
        wrong_validated_items = error.args[0].get('items')
        if wrong_validated_items :
            validated_items = error.valid_data

            for c in wrong_validated_items.keys():
                validated_items.get('items')[c] = None

            newlook = validated_items
        else:
            from werkzeug.exceptions import BadRequest
            raise BadRequest

    return LookService.upload_look(newlook)


@doc(tags=['looks'], description='코디의 컨펌여부')
@looks.route('/confirm', methods=['POST', 'GET'])
def confirm_codi():

    import requests

    response = requests.get('https://sherlockodds.blob.core.windows.net/musinsa/1159STUDIO_1477298_1_500.jpg')

    if response.status_code == 200:
        print(response.headers.get('Access-Control-Allow-Origin'))
    return "코디의 컨펌여부"
