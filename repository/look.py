from model.models import Look, Item
from sqlalchemy.sql.expression import func, or_
from model import db



def get_items(
    middlecategory=None, subcategory=None, brand=None, itemid=None, userid=None
) -> list:

    query = Item.query

    if subcategory:
        query = Item.query.filter(Item.subcategory.like(subcategory))
        if middlecategory and str(type(middlecategory)) == "<class 'str'>":
                query = query.filter(Item.category.like(middlecategory))

    if str(type(middlecategory)) == "<class 'list'>":
        query = Item.query.filter(
            or_(Item.category.like(middlecategory[0]), Item.category.like(middlecategory[1]))
        )

    elif str(type(middlecategory)) == "<class 'str'>" and not subcategory:
        query = query.filter(Item.category==middlecategory)

    if brand:
        query = query.filter(Item.brand == brand)

    # if itemid :
    #     query = query.filter(Item.id > itemid)


    results = query.order_by(func.random(userid)).paginate(page=itemid, per_page=12)
    return results.items


def add_look(items):

    new_look = Look(items)
    db.session.add(new_look)
    db.session.commit()

    return new_look


def delete_look(id):
    look = Look.query.get(id)
    db.session.delete(look)
    db.session.commit()
