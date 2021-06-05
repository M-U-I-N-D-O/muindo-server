from model import db
from model.models import User, Look, Item
from flask import jsonify

def my_looks_from_db(user_id):
    my_looks = Look.query.filter_by(userid=user_id).all()
    return my_looks



def my_look_detail_from_db(look_id:int) -> Look:
    look = Look.query.filter_by(id=look_id).first()
    return look


def item_info_from_db( hat_id, top_id, bottom_id, shoes_id, bag_id):
    hat_info = Item.query.filter_by(id=hat_id).first()
    top_info = Item.query.filter_by(id=top_id).first()
    bottom_info = Item.query.filter_by(id=bottom_id).first()
    shoes_info = Item.query.filter_by(id=shoes_id).first()
    bag_info = Item.query.filter_by(id=bag_id).first()
    return [hat_info, top_info, bottom_info, shoes_info, bag_info]
