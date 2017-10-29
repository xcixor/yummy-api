"""Defines the persistent entities used by the api"""
import re

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

    def __init__(self, username, password):
        """Creates a user with a username and password"""
        self.username = username
        self.password = password

    @staticmethod
    def validate_name(username):
        """Validates whether the username has special characters"""
        if re.match("^[a-zA-Z0-9 _]*$", username):
            return True
        return False        

    def save(self):
        """Saves a user to the database"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_user(username):
        """Find a user based on username"""
        return User.query.filter_by(username=username).first()

    def delete(self):
        """Deletes a user from the database"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Returns a string representation of the user"""
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

    def __init__(self, name, description, user_id):
        """Creates a category with the provided name, description and owner"""
        self.description = description
        self.name = name
        self,user_id = user_id
        

    def save(self):
        """Saves a category to the database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes a user from the database"""
        db.session.delete(self)
        db.session.commit()


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

    def __init__(self, name, ingredients, preparation, category_id):
        """Creates recipe with the provided attributes"""
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.category_id = category_id

    def save(self):
        """Saves a recipe to the database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes a recipe from the database"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Returns a string representation of the recipe"""
        return '<Recipe: {}>'.format(self.name)




