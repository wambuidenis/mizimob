from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField, SelectField, \
    MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from mizimob.models.models import User, Product, Category, CategorySchema

categories_schema = CategorySchema(many=True)
# categories_ = list()
categories_ = Category.query.all()
categories = [(x.name).lower().capitalize() for x in categories_]


class RegisterForm(FlaskForm):
    firstname = StringField("Firstname", validators=[DataRequired()])
    lastname = StringField("Lastname", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired()])
    password = PasswordField("Password",
                             validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Register")

    # validation from checking the email
    @staticmethod
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email Already Taken. Please Choose Another One")

    @staticmethod
    def validate_phone(self, phone):
        phone_length = len((phone.data)) >= 10
        if phone and not phone_length:
            raise ValidationError("Phone number not valid. Please enter a valid phone number.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# form for request user toe nter email for reset
class ResetRequest(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Request Email Reset")

    # validate password
    @staticmethod
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            flash("Email not found please Create an Account")


# form to confirm password
class ResetPassword(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=12)])
    verify = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=2, max=12)])
    submit = SubmitField("Request Email Reset")


class ProductForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    category = SelectField("Category", validators=[DataRequired()], choices=[(status, status) for status in categories])
    price = StringField("Price", validators=[DataRequired()])
    media = MultipleFileField("Images/Videos", validators=[DataRequired(), FileAllowed(["jpg", "png", "mp4", "mkv"])])
    description = TextAreaField("Description", validators=[DataRequired()])
    expires = StringField("When Post Expires", validators=[DataRequired()])
    active = RadioField("Active", choices=[(status, status) for status in ["Active", "Not Active"]])
    submit = SubmitField("Save The product")

    # validate password
    @staticmethod
    def validate_product(title):
        product = Product.query.filter_by(name=title.data).first()
        if product is not None:
            flash("Product With that name Exists. Please Use another name", "warning")


class CategoryForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Add Category")

    @staticmethod
    def validate_category(self, name):
        category = Category.query.filter_by(name=name.data).first()
        if category is not None:
            flash("Category Name Already Exists.", "warning")


class OrderForm(FlaskForm):
    phone = StringField("Phone Number", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    when = StringField("When", validators=[DataRequired()])
    where = StringField("Where", validators=[DataRequired()])
    submit = SubmitField("Make The Request")


class PhoneEmail(FlaskForm):
    email_phone = StringField("Email/Phone", validators=[DataRequired()])
    submit = SubmitField("Get Orders")


class CartForm(FlaskForm):
    submit = SubmitField("Add To Cart")
