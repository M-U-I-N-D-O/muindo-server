from model import db
from model.models import User, Look


def random_looks_from_db(user_id):
    random_looks = Look.query.filter(userid!=user_id).any()
    return random_looks


def test_looks_from_db(test):
    test_looks = Look.query.limit(test).all()
    return test_looks