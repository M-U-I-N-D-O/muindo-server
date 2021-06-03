from marshmallow import Schema, fields, validates_schema
from model.models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

@validates_schema()
class LookRequest(Schema):
    middlecategory = fields.String()
    subcategory = fields.String()
    brand = fields.String()
    type = fields.String()


class ItemSchema(SQLAlchemySchema):
    class Meta:
        model = Item

    id = auto_field()
    name = auto_field()
    url = auto_field()
    musinsa = auto_field()
    price = auto_field()
    brand = auto_field()


class ItemResponseShcema(SQLAlchemySchema):

    type = fields.String()
    data = fields.List(fields.Nested(ItemSchema))
