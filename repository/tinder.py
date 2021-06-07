from model.models import Look, Confirm
from model import db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

def random_looks_from_db(user_id=None, item_id=None):

    query = Look.query
    if item_id:
        query = query.filter(Look.id > item_id)

    random_looks = query.order_by().limit(12).all()
    return random_looks


def add_confirm(confirm):

    new_confirm = Confirm(confirm)
    db.session.add(new_confirm)
    try : db.session.commit()
    except IntegrityError as error:
        raise BadRequest

    return new_confirm.id

def get_confirm_info(lookid):

    confirms = Confirm.query.filter(Confirm.lookid == lookid).all()
    like , nope = 0 , 0

    for confirm in confirms:
        if confirm.yes :
            like += 1
        else:
            nope += 1

    return {'lookid' : lookid, 'like' : like, 'nope' : nope}