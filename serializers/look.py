from marshmallow import Schema, fields, ValidationError
from model.models import *
from marshmallow.fields import Nested, validate


class LookRequest(Schema):
    middlecategory = fields.String()
    subcategory = fields.String()
    brand = fields.String()
    type = fields.String()
    itemid = fields.Integer()


class ItemSchema(Schema):
    class Meta:
        model = Item

    id = fields.Integer()
    name = fields.String()
    url = fields.String()
    musinsa = fields.String()
    price = fields.Integer()
    brand = fields.String()


def validate_quantity(n):

    if n :
        raise ValueError





class ItemResponseShcema(Schema):

    type = fields.String()
    data = fields.Nested(Nested(ItemSchema))


class LookSchema(Schema):

    id = fields.Integer()
    userid = fields.Integer()
    hat = fields.Integer(validate=validate_quantity)
    top = fields.Integer(validate=validate_quantity)
    bottom = fields.Integer(validate=validate_quantity)
    shoes = fields.Integer(validate=validate_quantity)
    bag = fields.Integer(validate=validate_quantity)
    url = fields.String()
    ok = fields.Integer()
    no = fields.Integer()


class MakeLookRequestSchema(Schema):
    dataType = fields.String(validate=validate_quantity)
    items = Nested(LookSchema)
