from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from service.solution import *
from serializers.solution import *
from decorators.view import auth_required


solution = Blueprint("solution", __name__, url_prefix="/solution")

@auth_required(tags=['solution'], description='솔루션 예시 코디 가져오기')
@solution.route('/samples', methods=['GET'])
@use_kwargs(SolutionSampleRequest, location='query')
@marshal_with(SolutionCodi(many=True))
def get_sample_codis(**kwargs):

    return SolutionService.get_codis_filtered_gender(kwargs.get('gender'))

