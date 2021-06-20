from marshmallow import Schema, fields, ValidationError,validates


class TokensSchema(Schema):
    class Meta:
        access_token = fields.Str()
        refresh_token = fields.Str()


class AccessTokenSchema(Schema):
    class Meta:
        access_token = fields.Str()


class GetTokensRequestSchema(Schema):
    uid = fields.String()
    email = fields.Email()
    name = fields.String()
    provider = fields.String()

    @validates('provider')
    def validate(self, provider):
        if provider not in ["KAKAO", "PASSWORD", "GOOGLE"]:
            raise ValidationError('올바른 아이디 인증기관이 아닙니다.')

