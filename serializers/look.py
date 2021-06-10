from marshmallow import Schema, fields, pre_load, pre_dump
from model.models import *



def validte_type(n):
    if n == '':
        n= None
    return n

class LookRequest(Schema):
    middlecategory = fields.String(allow_none=True)
    subcategory = fields.String(allow_none=True)
    brand = fields.String(allow_none=True)
    type = fields.String(required=True)
    itemid = fields.String(allow_none=True)

    @pre_load
    def check_value(self, data, **kwargs):
        filters = {}
        for k, v in data.data.items():
            filters[k] = validte_type(v)

        from werkzeug.datastructures import ImmutableMultiDict
        new_data = ImmutableMultiDict(filters.items())
        return new_data


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
    hat = fields.Integer(allow_none=True)
    top = fields.Integer(allow_none=True)
    bottom = fields.Integer(allow_none=True)
    shoes = fields.Integer(allow_none=True)
    bag = fields.Integer(allow_none=True)
    url = fields.String()
    ok = fields.Integer()
    no = fields.Integer()
    tpo = fields.String()

class MakeLookRequest(Schema):

    dataType = fields.String()
    data = fields.Nested(Schema.from_dict({"img" : fields.String()}))
    items = fields.Nested(LookSchema, only=('tpo','top', 'hat', 'bottom', 'shoes', 'bag'))
    tpo = fields.String(allow_none=True)

    @pre_load
    def check_none(self, data, **kwargs):

        for k , v in data.get('items').items():
            if v == '':
                data.get('items')[k] = None

        if data.get('tpo') != '':
            data.get('items')['tpo'] = data.get('tpo')

        return data