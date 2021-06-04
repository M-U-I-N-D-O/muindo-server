from model.models import Look, Item
from sqlalchemy.sql.expression import func
from model import db

def get_user_looks(userid:int) -> list:
    looks = Look.query.all()
    return []


def get_look(lookid:int) -> Look:
    look = Look.query.filter(lookid)
    return Look()


def get_items(middlecategory=None, subcategory=None, brand=None) -> list:

    query = Item.query

    if middlecategory:
        query = query.filter(Item.category.like(middlecategory))

    if subcategory:
        query = query.filter(Item.subcategory.like(subcategory))

    if brand:
        query = query.filter(Item.brand==brand)


    results = query.order_by(func.random()).limit(12).all()

    db.session.close()

    return results


def add_look(items):

    new_look = Look(items)
    db.session.add(new_look)
    db.session.close()

    return new_look.id



