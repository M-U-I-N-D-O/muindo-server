from model.models import Look, Item


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

    return query.all()