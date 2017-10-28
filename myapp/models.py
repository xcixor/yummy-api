"""Defines the persistent entities used by the api"""

from . import db

class User(db.Model):
    """
    Defines the user table
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True)
    password = db.Column(db.String(256), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), \
    onupdate=db.func.current_timestamp())
    categories = db.relationship('Category', backref='user')

    def save(self):
        """Saves a user to the database"""
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User: {}>'.format(self.username)

class Category(db.Model):
    """Defines the table for categories"""
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), \
    onupdate=db.func.current_timestamp())
    recipes = db.relationship('Recipe', backref='category')

    def __repr__(self):
        return '<Category: {}, Description: {}>'.format(self.name, self.description)
class Recipe(db.Model):
    """Defines the recipe table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    ingredients = db.Column(db.String(255))
    preparation = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), \
    onupdate=db.func.current_timestamp())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Recipe: {}, Preparation: {}>'.format(self.name, self.preparation)




