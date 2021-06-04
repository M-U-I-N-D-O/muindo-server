from model import db
from model.models import User, Look


def my_looks_from_db(unique_id):
    user_id = User.query.filter_by(uid=unique_id).id
    my_looks = Look.query.filter_by(userid=user_id).all()
    return my_looks



def my_look_detail_from_db(look_id:int) -> Look:
    look = Look.query.filter(look_id)
    return look