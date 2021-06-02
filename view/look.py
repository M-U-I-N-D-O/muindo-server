from flask import Blueprint
from flask_apispec import doc, use_kwargs
from serializers.look import LookRequest
looks = Blueprint("looks", __name__, url_prefix="/looks")


@doc(tags=['looks'], description='필터 조건에 따라 무신사 아이템들을 보여줌.')
@looks.route('/items')
@use_kwargs(LookRequest, location="query")
def get_musinsa_items(**kwargs):
    print(kwargs.items())
    return "필터 조건에 따라 무신사 아이템들을 보여줌."


@doc(tags=['looks'], description='조합한 아이템들을 코디로 만듬')
@looks.route('/upload', methods=['POST'])
def upload_codi():

    return "조합한 아이템들을 코디로 만듬"


@doc(tags=['looks'],description='코디의 컨펌여부')
@looks.route('/confirm', methods=['POST'])
def confirm_codi():

    return "코디의 컨펌여부"




