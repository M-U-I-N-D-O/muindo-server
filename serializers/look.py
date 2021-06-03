from flask_marshmallow import Schema, sqla, Marshmallow as ma
from flask_marshmallow.fields import fields
from model.models import Item


class LookRequest(Schema):
    middlecategory = fields.String()
    subcategory = fields.String()
    brand = fields.String()


class ItemSchema(Schema):
    class Meta:
        url = fields.String()