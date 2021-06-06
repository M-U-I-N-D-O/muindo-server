from marshmallow import Schema, fields, validates_schema
from model.models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class MyLooksSchema(SQLAlchemySchema):
    class Meta:
        model = Look
    id = auto_field()
    created = auto_field()
    userid = auto_field()
    hat = auto_field()
    top = auto_field()
    bottom = auto_field()
    shoes = auto_field()
    bag = auto_field()
    ok = auto_field()
    no = auto_field()
    url = auto_field()


class GetItemInfoSchema(Schema):
    hat_id = fields.Integer()
    top_id = fields.Integer()
    bottom_id = fields.Integer()
    shoes_id = fields.Integer()
    bag_id= fields.Integer()


class ItemsInfoSchema(SQLAlchemySchema):
    class Meta:
        model = Item
    id = auto_field()
    name = auto_field()
    url = auto_field()
    musinsa = auto_field()
    price = auto_field()
    brand = auto_field()

