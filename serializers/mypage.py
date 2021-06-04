from marshmallow import Schema, fields, validates_schema
from model.models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class MyLooksSchema(SQLAlchemySchema):
    class Meta:
        model = Look

    id = auto_field()
    created = auto_field()
    userid = auto_field()
    hat = auto_field()
    top = auto_field()
    bottom = auto_field()
    shoes = auto_field()
    bag = auto_field()
    ok = auto_field()
    no = auto_field()