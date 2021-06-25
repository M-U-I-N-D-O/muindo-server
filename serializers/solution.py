from marshmallow import Schema, fields, pre_load, pre_dump
from model.models import *


class SolutionSampleRequest(Schema):
    gender = fields.String(allow_none=True)

    @pre_load
    def check_none(self, data, **kwargs):

        if data.get('gender') == '':
            from werkzeug.datastructures import ImmutableMultiDict
            new_data = ImmutableMultiDict({'gender' : None})
            return new_data

        return data


class SolutionCodi(Schema):

    title = fields.String()
    url = fields.String()
    type = fields.String()
    gender = fields.String()

