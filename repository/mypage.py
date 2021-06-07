from model import db
from model.models import Look, Item


def my_looks_from_db(user_id):
    my_looks = Look.query.filter_by(userid=user_id).all()
    return my_looks



def my_look_detail_from_db(look_id:int) -> Look:
    look = Look.query.filter_by(id=look_id).first()
    return look


def item_info_from_db(items:dict):

    hat = Item.query.filter_by(id=items.get('hat_id')).first()
    top = Item.query.filter_by(id=items.get('top_id')).first()
    bottom = Item.query.filter_by(id=items.get('bottom_id')).first()
    shoes = Item.query.filter_by(id=items.get('shoes_id')).first()
    bag = Item.query.filter_by(id=items.get('bag_id')).first()

    return {"hat" : hat, "top" : top, "bottom" : bottom, "shoes" : shoes, "bag" : bag}
