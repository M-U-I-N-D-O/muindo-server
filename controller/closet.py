from flask import Blueprint
from flask_restful import wraps

closet = Blueprint("closet", __name__, url_prefix="/closet")

def access_token_required(f):
    f.__access_token_required = True

    @wraps(f)
    def decorated(*args, **kwargs):
        print('do_something_with_access_token')

        return f(*args, **kwargs)

    return decorated

@closet.route("")
@access_token_required
def get_all_looks():

    return "모든 코디를 조회해서 보여줌."



