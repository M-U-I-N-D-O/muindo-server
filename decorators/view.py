from flask_jwt_extended import jwt_required,verify_jwt_in_request
from flask_apispec import doc
import functools

def auth_required(tags, description, refresh=False):
    def inner(func):
        if refresh:
            params ={'Authorization': {
            'description':
            'Authorization HTTP header with JWT Refresh token,'
            'like: Authorization: Bearer asdf.qwer.zxcv',
            'in':'header',
            'type':'string',
            'required': True}}
            wrapped = doc(tags=tags, description=description, params=params)(func)
            wrapped2 = jwt_required(refresh=True)(wrapped)
            return wrapped2
        else:
            params ={'Authorization': {
                'description':
                'Authorization HTTP header with JWT Access token,'
                'like: Authorization: Bearer asdf.qwer.zxcv',
                'in':'header',
                'type':'string',
                'required': True}}
            wrapped = doc( tags=tags,description=description,params=params)(func)
            wrapped2 = jwt_required()(wrapped)
            return wrapped2
    return inner
