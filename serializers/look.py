from marshmallow import Schema, fields, validates_schema
from model.models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested

@validates_schema()
class LookRequest(Schema):
    middlecategory = fields.String()
    subcategory = fields.String()
    brand = fields.String()
    type = fields.String()
    itemid = fields.Integer()

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


class LookSchema(SQLAlchemySchema):

    class Meta:
        model = Look

    id = auto_field()
    userid = auto_field()
    hat = auto_field()
    top = auto_field()
    bottom = auto_field()
    shoes = auto_field()
    bag = auto_field()
    url = auto_field()
    ok = auto_field()
    no = auto_field()
