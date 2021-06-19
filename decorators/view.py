from flask_jwt_extended import jwt_required
from flask_apispec import doc


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
            wrapped = jwt_required(refresh=True)(wrapped)
            return wrapped

        params ={'Authorization': {
            'description':
            'Authorization HTTP header with JWT Access token,'
            'like: Authorization: Bearer asdf.qwer.zxcv',
            'in':'header',
            'type':'string',
            'required': True}}
        wrapped = doc( tags=tags,description=description,params=params)(func)
        wrapped = jwt_required()(wrapped)
        return wrapped
    return inner