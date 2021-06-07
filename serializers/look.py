from marshmallow import Schema, fields
from model.models import *


def validate_item(n):

    if n == '':
        print('nope')
        n = -1

class LookRequest(Schema):
    middlecategory = fields.String(default='', required=False)
    subcategory = fields.String(default='', required=False)
    brand = fields.String(default='', required=False)
    type = fields.String(default='', required=False)
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


class ItemResponseShcema(Schema):

    type = fields.String()
    data = fields.List(fields.Nested(ItemSchema))


class LookSchema(Schema):

    class Meta:
        model = Look

    id = fields.Integer()
    userid = fields.Integer()
    hat = fields.Integer(validate=validate_item, default=0)
    top = fields.Integer(validate=validate_item)
    bottom = fields.Integer(validate=validate_item)
    shoes = fields.Integer(validate=validate_item)
    bag = fields.Integer(validate=validate_item)
    url = fields.String()
    ok = fields.Integer()
    no = fields.Integer()

class MakeLookRequest(Schema):

    dataType = fields.String()
    data = fields.Nested(Schema.from_dict({"img" : fields.String()}))
    items = fields.Nested(LookSchema)
