from model.models import Look, Confirm
from model import db

def random_looks_from_db(user_id=None, item_id=None):

    query = Look.query
    if item_id:
        query = query.filter(Look.id > item_id)

    random_looks = query.order_by().limit(12).all()
    return random_looks


def add_confirm(confirm):

    new_confirm = Confirm(confirm)
    db.session.add(new_confirm)
    db.session.commit()

    return new_confirm.id