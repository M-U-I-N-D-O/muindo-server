from flask_sqlalchemy import SQLAlchemy as db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.ForeignKey('user.id'), index=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime)
    rating = db.Column(db.Integer)
    postid = db.Column(db.ForeignKey('post.id'), index=True)

    post = db.relationship('Post', primaryjoin='Comment.postid == Post.id', backref='comments')
    user = db.relationship('User', primaryjoin='Comment.userid == User.id', backref='comments')



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
    attr_1 = db.Column(db.Integer, server_default=db.FetchedValue())
    attr_2 = db.Column(db.Integer, server_default=db.FetchedValue())
    attr_3 = db.Column(db.Integer, server_default=db.FetchedValue())
    attr_4 = db.Column(db.Integer, server_default=db.FetchedValue())
    attr_5 = db.Column(db.Integer, server_default=db.FetchedValue())
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

    item = db.relationship('Item', primaryjoin='Look.bag == Item.id', backref='item_item_item_item_looks')
    item1 = db.relationship('Item', primaryjoin='Look.bottom == Item.id', backref='item_item_item_item_looks_0')
    item2 = db.relationship('Item', primaryjoin='Look.hat == Item.id', backref='item_item_item_item_looks')
    item3 = db.relationship('Item', primaryjoin='Look.shoes == Item.id', backref='item_item_item_item_looks_0')
    item4 = db.relationship('Item', primaryjoin='Look.top == Item.id', backref='item_item_item_item_looks')
    user = db.relationship('User', primaryjoin='Look.userid == User.id', backref='looks')



class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    lookid = db.Column(db.ForeignKey('look.id'), index=True)
    userid = db.Column(db.ForeignKey('user.id'), index=True)
    created = db.Column(db.DateTime)

    look = db.relationship('Look', primaryjoin='Post.lookid == Look.id', backref='posts')
    user = db.relationship('User', primaryjoin='Post.userid == User.id', backref='posts')



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



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    _pass = db.Column('pass', db.String(45))
    oauth = db.Column(db.String(10))
