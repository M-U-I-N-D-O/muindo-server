from marshmallow import Schema, fields


class ConfirmSchema(Schema):
    yes = fields.Boolean()
    no = fields.Boolean()
    userid = fields.Integer()



