from model.models import Look, Confirm, Thumb
from model import db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from datetime import datetime

def random_looks_from_db(user_id=None, item_id=None):

    query = Look.query
    if item_id:
        query = query.filter(Look.id > item_id)

    random_looks = query.order_by().limit(12).all()
    return random_looks


def update_look_info(confirm, lookid):
    look = Look.query.get(lookid)
    if confirm:
        look.ok += 1
    else:
        look.no += 1

    db.session.commit()


def add_confirm(confirm):

    new_confirm = Confirm(confirm)
    db.session.add(new_confirm)
    try : db.session.commit()
    except IntegrityError:
        raise BadRequest

    return new_confirm.id


def get_confirm_info(lookid):
    look = Look.query.filter(Look.id == lookid).first()
    return {'lookid' : lookid, 'like' : look.ok, 'nope' : look.no}


def add_thumb(user_id, look_id):
    new_thumb = Thumb(userid=user_id, lookid=look_id, created = datetime.now())
    db.session.add(new_thumb)
    db.session.commit()
    return new_thumb.id
