from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main_db.db'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    hash = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.username

class Parties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Parties %r>' % self.name

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    level = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    party_id = db.Column(db.Integer, db.ForeignKey('parties.id'))
    stats = db.Column(db.PickleType)
    abilities = db.Column(db.PickleType)
    armor_slots = db.Column(db.PickleType)
    backpack = db.Column(db.PickleType)

    def __repr__(self):
        return '<Characters %r>' % self.name
