from model import db
from model.models import User, Look


def get_my_looks(unique_id):
    user_id = User.query.filter_by(uid=unique_id).id
    my_looks = Look.query.filter_by(userid=user_id).all()
    return my_looks



def get_look(lookid:int) -> Look:
    look = Look.query.filter(lookid)
    return Look()