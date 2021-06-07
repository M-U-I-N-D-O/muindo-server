from model.models import Look, Item
from sqlalchemy.sql.expression import func, or_
from model import db


def get_initial_items(type, userid, itemid):

    results = (
        Item.query.filter(or_(Item.category.like(type[0]), Item.category.like(type[1])))
        .filter(Item.id > itemid)
        .order_by(func.rand(userid))
        .limit(12)
        .all()
    )
    return sorted(results, key=lambda x: x.id)


def get_items(
    middlecategory=None, subcategory=None, brand=None, itemid=None, userid=None
) -> list:

    query = Item.query

    if subcategory:
        query = query.filter(Item.subcategory.like(subcategory))

    if brand:
        query = query.filter(Item.brand == brand)

    if itemid:
        query = query.filter(Item.id > itemid)

    if middlecategory and not subcategory:
        query = Item.query.filter(Item.category == middlecategory)

    results = query.order_by(func.rand(userid)).limit(12).all()
    return sorted(results, key=lambda x: x.id)


def add_look(items):

    new_look = Look(items)
    db.session.add(new_look)
    db.session.commit()

    return new_look
