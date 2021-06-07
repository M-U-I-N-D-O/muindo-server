from marshmallow import Schema, fields
from model.models import *



def validte_type(n):

    if n == '':
        pass

class LookRequest(Schema):
    middlecategory = fields.String()
    subcategory = fields.String()
    brand = fields.String()
    type = fields.String(required=True)
    itemid = fields.String()


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
    hat = fields.Integer()
    top = fields.Integer()
    bottom = fields.Integer()
    shoes = fields.Integer()
    bag = fields.Integer()
    url = fields.String()
    ok = fields.Integer()
    no = fields.Integer()

class MakeLookRequest(Schema):

    dataType = fields.String()
    data = fields.Nested(Schema.from_dict({"img" : fields.String()}))
    items = fields.Nested(LookSchema)
