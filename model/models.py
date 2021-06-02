# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


model = SQLAlchemy()



class Item(model.Model):
    __tablename__ = 'item'

    id = model.Column(model.Integer, primary_key=True)
    name = model.Column(model.String(100))
    url = model.Column(model.String(100))
    color = model.Column(model.String(45))
    category = model.Column(model.String(45))
    updated = model.Column(model.DateTime)
    brand = model.Column(model.String(45))
    subcategory = model.Column(model.String(45))
    price = model.Column(model.Integer)
    musinsa = model.Column(model.String(100))
    itemno = model.Column(model.String(45))



class Look(model.Model):
    __tablename__ = 'look'

    id = model.Column(model.Integer, primary_key=True)
    created = model.Column(model.DateTime)
    userid = model.Column(model.ForeignKey('user.id'), index=True)
    hat = model.Column(model.ForeignKey('item.id'), index=True)
    top = model.Column(model.ForeignKey('item.id'), index=True)
    bottom = model.Column(model.ForeignKey('item.id'), index=True)
    shoes = model.Column(model.ForeignKey('item.id'), index=True)
    bag = model.Column(model.ForeignKey('item.id'), index=True)
    ok = model.Column(model.Integer)
    no = model.Column(model.Integer)

    item = model.relationship('Item', primaryjoin='Look.bag == Item.id', backref='item_item_item_item_looks')
    item1 = model.relationship('Item', primaryjoin='Look.bottom == Item.id', backref='item_item_item_item_looks_0')
    item2 = model.relationship('Item', primaryjoin='Look.hat == Item.id', backref='item_item_item_item_looks')
    item3 = model.relationship('Item', primaryjoin='Look.shoes == Item.id', backref='item_item_item_item_looks_0')
    item4 = model.relationship('Item', primaryjoin='Look.top == Item.id', backref='item_item_item_item_looks')
    user = model.relationship('User', primaryjoin='Look.userid == User.id', backref='looks')



class Style(model.Model):
    __tablename__ = 'style'

    id = model.Column(model.Integer, primary_key=True)
    url = model.Column(model.String(100))
    gender = model.Column(model.Integer)
    type = model.Column(model.String(45))
    title = model.Column(model.String(45))
    item_1 = model.Column(model.Integer)
    item_2 = model.Column(model.Integer)
    item_3 = model.Column(model.Integer)
    item_4 = model.Column(model.Integer)
    item_5 = model.Column(model.Integer)
    item_6 = model.Column(model.Integer)
    musinsa = model.Column(model.String(100))



class User(model.Model):
    __tablename__ = 'user'

    id = model.Column(model.Integer, primary_key=True)
    name = model.Column(model.String(45))
    email = model.Column(model.String(45))
    oauth = model.Column(model.String(10))
    uid = model.Column(model.String(45))
