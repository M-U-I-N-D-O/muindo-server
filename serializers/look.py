from marshmallow import Schema, fields

class LookRequest(Schema):
    middlecategory = fields.Integer()
    subcategory = fields.Integer()
    brand = fields.String()