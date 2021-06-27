from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask import jsonify
from repository.auth import *


def if_first_time_insert_db_and_get_user_id(email, name, provider, unique_id):
    return db_check_if_not_insert_to_db_and_get_user_id(email, name, provider, unique_id)

def guest_login(email, name, provider, unique_id):
    return guset_insert_to_db(email, name, provider, unique_id)



class AuthService:
    @classmethod
    def create_tokens(self, user_id):
        access_token = create_access_token(identity=user_id, fresh=True)
        refresh_token = create_refresh_token(identity=user_id)
        return {"access_token": access_token, "refresh_token": refresh_token}

    @classmethod
    def create_access_token(self,user_id):
        access_token = create_access_token(identity=user_id, fresh=False)
        return jsonify(access_token=access_token)
