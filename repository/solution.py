from model.models import Style
from sqlalchemy.sql.expression import func
import random

def get_styles_gender(gender):

    if gender:
        styles = Style.query.filter(Style.gender == gender).order_by(func.rand(random.randint(0, 10))).limit(100).all()

    else:
        styles = Style.query.order_by(func.rand(random.randint(0, 10))).limit(100).all()

    return styles