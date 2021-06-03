from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

from repository.auth import db_check_if_not_insert_to_db


def if_first_time_insert_db(email, name, provider, unique_id):
    db_check_if_not_insert_to_db(email, name, provider, unique_id)


def create_tokens(unique_id):
    access_token = create_access_token(identity=unique_id, fresh=True)
    refresh_token = create_refresh_token(identity=unique_id)
    return access_token, refresh_token


