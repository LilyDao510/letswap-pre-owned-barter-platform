from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Items(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

class ExchangeRequests(db.Model):
    __tablename__ = 'exchange_requests'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    requester_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=db.func.current_timestamp())
    address = db.Column(db.String(255))
    shipping_type = db.Column(db.String(255))

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=db.func.current_timestamp())
    exchange_request_id = db.Column(db.Integer, db.ForeignKey('exchange_requests.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))