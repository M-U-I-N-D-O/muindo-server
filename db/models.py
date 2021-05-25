from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.VARCHAR(45), unique_key=True)
    email = db.Column(db.VARCHAR(45), unique_key=True)
    name = db.Column(db.VARCHAR(45))