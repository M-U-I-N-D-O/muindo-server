from marshmallow import Schema, fields, validate


class ConfirmSchema(Schema):
    id = fields.Integer()
    opinion = fields.String(validate=validate.OneOf(["like", "nope"]))
    token = fields.String()


class LookConfirmInfo(Schema):

    lookid = fields.Integer()
    like = fields.Integer()
    nope = fields.Integer()


class UpdateThumb(Schema):
    lookid =  fields.Integer(),
    value = fields.Boolean()



