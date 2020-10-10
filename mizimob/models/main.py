from flask_login import UserMixin
from mizimob import db,ma, login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# we are going to create the model from a user class
# the user mixen adds certain fields that are required matain the use session
# it will add certain fileds to the user class tha are essential to the user login


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), unique=True, nullable=False)
    lastname = db.Column(db.String(100),unique=True, nullable=False)
    phone = db.Column(db.String(100),unique=True)
    email = db.Column(db.String(48), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User (' {self.id} ',' {self.username} ', '{self.email}', '{self.image_file}' )"

    def __init__(self, firstname, lastname, phone, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","firstname","lastname","phone","email","password")


# creating a company class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.now)
    category = db.Column(db.ForeignKey('category.id'),nullable=False)
    price = db.Column(db.Integer,nullable=False,default=10)
    media = db.Column(db.Text,nullable=False, default="default.png")
    expires = db.Column(db.String(100),nullable=False)

    def __init__(self,name,description,category,price,media,expires):
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.media = media
        self.expires = expires


class CategorySChema(ma.Schema):
    class Meta:
        fields = ("id","name","category","price","media","expires","date_added")


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)

    def __init__(self,name):
        self.name = name


class CategorySchema(ma.Schema):
    class Meta:
        fields = ("id","name")

