from flask_jwt_extended import create_access_token,set_access_cookies
from flask_jwt_extended import create_refresh_token
from flask import jsonify
from repository.auth import db_check_if_not_insert_to_db

def if_first_time_insert_db(email, name, provider, unique_id):
    db_check_if_not_insert_to_db(email, name, provider, unique_id)


class AuthService:
    @classmethod
    def create_tokens(self, user_id):
        try:
            access_token = create_access_token(identity=user_id, fresh=True)
            response=jsonify({"msg": "login successful"})
            set_access_cookies(response, access_token)
            return response
        except:
            return jsonify({"msg":"login fail"})

    @classmethod
    def create_access_token(self,user_id):
        access_token = create_access_token(identity=user_id, fresh=False)
        return jsonify(access_token=access_token)