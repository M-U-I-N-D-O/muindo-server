from marshmallow import Schema, fields, validate


class ConfirmSchema(Schema):
    id = fields.Integer()
    opinion = fields.String(validate=validate.OneOf(["like", "nope"]))
    token = fields.String()



