from flask import Blueprint
from flask_apispec import doc

mypage = Blueprint("mypage", __name__, url_prefix="/mypage")

@doc(tags=['mypage'], description='해당 코디 정보들을 조회함.')
@mypage.route('/mylooks')
def get_looks(lookid):

    return "해당 코디 정보들을 조회함."