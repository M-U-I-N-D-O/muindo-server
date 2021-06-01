from model.models import Look


def get_user_looks(userid:int) -> list:
    looks = Look.query.all()
    return []


def get_look(lookid:int) -> Look:
    look = Look.query.filter(lookid)
    return Look()