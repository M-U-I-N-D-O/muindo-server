from marshmallow import Schema, fields
from serializers.look import ItemSchema

class GetItemInfoSchema(Schema):
    hat_id = fields.String()
    top_id = fields.String()
    bottom_id = fields.String()
    shoes_id = fields.String()
    bag_id= fields.String()


class ItemsInfoSchema(Schema):

    id = fields.Integer()
    lookBookImgUrl = fields.String()
    hat = fields.Nested(ItemSchema)
    top = fields.Nested(ItemSchema)
    bottom = fields.Nested(ItemSchema)
    bag = fields.Nested(ItemSchema)
    shoes = fields.Nested(ItemSchema)
