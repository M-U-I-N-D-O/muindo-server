from marshmallow import Schema, fields, ValidationError

class Tokens:
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token

class TokensSchema(Schema):
    class Meta:
        msg = fields.Str()


class AccessTokenSchema(Schema):
    class Meta:
        access_token = fields.Str()



class GetTokensRequestSchema(Schema):
    uid = fields.String()
    email = fields.Email()
    name = fields.String()
    provider = fields.String()




