from model.models import Look, Item
from sqlalchemy.sql.expression import func, or_
from model import db

def get_items(middlecategory=None, subcategory=None, brand=None, itemid=None, userid=None) -> list:

    query = Item.query

    if middlecategory:
        query = query.filter(or_(Item.category.like(middlecategory[0]), Item.category.like(middlecategory[1])))


    if subcategory:
        query = query.filter(Item.subcategory.like(subcategory))

    if brand:
        query = query.filter(Item.brand==brand)

    if itemid:
        query = query.filter(Item.id > itemid)

    results = query.order_by(func.rand(userid)).limit(12).all()
    return sorted(results, key=lambda x : x.id)


def add_look(items):

    new_look = Look(items)
    db.session.add(new_look)
    db.session.commit()

    return new_look



