from flask import Blueprint, request
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.look import LookRequest, LookSchema, ItemSchema, MakeLookRequest
from service.look import ItemService, LookService
from flask_jwt_extended import jwt_required


looks = Blueprint("looks", __name__, url_prefix="/looks")


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items', methods=['GET'])
@use_kwargs(LookRequest, location='query')
@jwt_required()
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(**filter):
    filter = request.args
    filter = filter.to_dict()
    return ItemService.get_musinsa_items(filter)


@doc(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@looks.route('/upload', methods=['POST'])
@use_kwargs(MakeLookRequest)
@jwt_required()
@marshal_with(LookSchema)
def upload_codi(**kwargs):
    schema = MakeLookRequest()

    newlook = schema.load(request.get_json())

    return LookService.upload_look(newlook)


@doc(tags=['looks'], description='나의 룩북 삭제')
@looks.route('/remove', methods=['DELETE'])
def remove_look():
    return 'remove look'