from flask import request
from marshmallow import Schema, fields, ValidationError

class Tokens:
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token

class TokensSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()


def SerializeTokens(access_token, refresh_token):
    tokens = Tokens(access_token, refresh_token)
    schema = TokensSchema()
    serialized_tokens = schema.dumps(tokens)
    return serialized_tokens


class GetTokensRequestSchema(Schema):
    uid = fields.String(
        required=True,
        metadata={
            "description" : "유저 고유값 아이디",
            "example": "asdwqdwasd"
        },

    )
    email = fields.Email(
        required=True,
        metadata={
            "description" : "이메일",
            "example": "elon4856@naver.com"
        },)
    name = fields.String(
        required=True,
        metadata={
            "description" : "유저 닉네임",
            "example": "따라란"
        },)
    provider = fields.String(
        required=True,
        metadata={
            "description": "로그인 제공자",
            "example": "google"
        },
    )

def deserialize_request(data):
    get_tokens_request_schema = GetTokensRequestSchema()
    payload = get_tokens_request_schema.load(data)
    unique_id = payload['uid']
    email = payload['email']
    name = payload['name']
    provider = payload['provider']
    return email, name, provider, unique_id


