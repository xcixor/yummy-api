"""Defines the persistent entities used by the api"""

from . import db

class User(db.Model):
    """Defines the user table"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True)
    password = db.Column(db.String(256), nullable=False, unique=True)
    categories = db.relationship('Category', backref = 'user')

    def __repr__(self):
        return '<User: {}>'.format(self.username)

class Category(db.Model):
    """Defines the table for categories"""
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    description = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipes = db.relationship('Recipe', backref = 'category')

    def __repr__(self):
        return '<Category: {}, Description: {}>'.format(self.name, self.description)
class Recipe(db.Model):
    """Defines the recipe table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, unique=True)
    ingredients = db.Column(db.String(256))
    preparation = db.Column(db.String(256))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Recipe: {}, Preparation: {}>'.format(self.name, self.preparation)




