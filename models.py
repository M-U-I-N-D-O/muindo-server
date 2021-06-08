# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Confirm(db.Model):
    __tablename__ = 'confirm'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.ForeignKey('user.id'), index=True)
    lookid = db.Column(db.ForeignKey('look.id'), index=True)
    yes = db.Column(db.Integer)
    no = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    look = db.relationship('Look', primaryjoin='Confirm.lookid == Look.id', backref='confirms')
    user = db.relationship('User', primaryjoin='Confirm.userid == User.id', backref='confirms')



class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(100))
    color = db.Column(db.String(45))
    category = db.Column(db.String(45))
    updated = db.Column(db.DateTime)
    brand = db.Column(db.String(45))
    subcategory = db.Column(db.String(45))
    price = db.Column(db.Integer)
    musinsa = db.Column(db.String(100))
    itemno = db.Column(db.String(45))



class Look(db.Model):
    __tablename__ = 'look'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    userid = db.Column(db.ForeignKey('user.id'), index=True)
    hat = db.Column(db.ForeignKey('item.id'), index=True)
    top = db.Column(db.ForeignKey('item.id'), index=True)
    bottom = db.Column(db.ForeignKey('item.id'), index=True)
    shoes = db.Column(db.ForeignKey('item.id'), index=True)
    bag = db.Column(db.ForeignKey('item.id'), index=True)
    ok = db.Column(db.Integer, server_default=db.FetchedValue())
    no = db.Column(db.Integer, server_default=db.FetchedValue())
    url = db.Column(db.String(100))
    thumbs = db.Column(db.Integer, server_default=db.FetchedValue())

    item = db.relationship('Item', primaryjoin='Look.bag == Item.id', backref='item_item_item_item_looks')
    item1 = db.relationship('Item', primaryjoin='Look.bottom == Item.id', backref='item_item_item_item_looks_0')
    item2 = db.relationship('Item', primaryjoin='Look.hat == Item.id', backref='item_item_item_item_looks')
    item3 = db.relationship('Item', primaryjoin='Look.shoes == Item.id', backref='item_item_item_item_looks_0')
    item4 = db.relationship('Item', primaryjoin='Look.top == Item.id', backref='item_item_item_item_looks')
    user = db.relationship('User', primaryjoin='Look.userid == User.id', backref='looks')



class Style(db.Model):
    __tablename__ = 'style'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))
    gender = db.Column(db.Integer)
    type = db.Column(db.String(45))
    title = db.Column(db.String(45))
    item_1 = db.Column(db.Integer)
    item_2 = db.Column(db.Integer)
    item_3 = db.Column(db.Integer)
    item_4 = db.Column(db.Integer)
    item_5 = db.Column(db.Integer)
    item_6 = db.Column(db.Integer)
    musinsa = db.Column(db.String(100))



class Thumb(db.Model):
    __tablename__ = 'thumb'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.ForeignKey('user.id'), index=True)
    lookid = db.Column(db.ForeignKey('look.id'), index=True)
    created = db.Column(db.DateTime)

    look = db.relationship('Look', primaryjoin='Thumb.lookid == Look.id', backref='thumbs')
    user = db.relationship('User', primaryjoin='Thumb.userid == User.id', backref='thumbs')



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    oauth = db.Column(db.String(10))
    uid = db.Column(db.String(45))
