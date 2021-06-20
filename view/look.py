from flask import Blueprint, request, Response
from flask_apispec import use_kwargs, marshal_with
from serializers.look import LookRequest, LookSchema, ItemSchema, MakeLookRequest
from service.look import ItemService, LookService
from decorators.view import auth_required

looks = Blueprint("looks", __name__, url_prefix="/looks")



@looks.route('/items', methods=['GET'])
@auth_required(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@use_kwargs(LookRequest, location='query')
@marshal_with(ItemSchema(many=True))
def get_musinsa_items(**filter):
    filter = request.args
    filter = filter.to_dict()
    return ItemService.get_musinsa_items(filter)


@looks.route('/upload', methods=['POST'])
@auth_required(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@use_kwargs(MakeLookRequest)
@marshal_with(LookSchema)
def upload_codi(**kwargs):
    schema = MakeLookRequest()

    newlook = schema.load(request.get_json())

    return LookService.upload_look(newlook)


@looks.route('/remove/<int:lookid>', methods=['DELETE'])
@auth_required(tags=['looks'], description='나의 룩북 삭제')
def remove_look(lookid):
    LookService.remove_look(lookid)
    return Response(status=200)