from model.models import Look


def random_looks_from_db(user_id=None, item_id=None):

    query = Look.query
    if item_id:
        query = query.filter(Look.id > item_id)

    random_looks = query.order_by().limit(12).all()
    return random_looks


def test_looks_from_db(test):
    test_looks = Look.query.limit(test).all()
    return test_looks