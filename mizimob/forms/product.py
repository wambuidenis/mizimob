from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
from mizimob.models.main import User,Product,Category
from flask import flash


class RegisterForm(FlaskForm):
    firstaname = StringField("Firstname", validators=[DataRequired() ])
    lastname = StringField("Lastname", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Register")

    # validation  for checking if the username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username Already Taken. Please Choose Another One")

    # validation from checking the email
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email Already Taken. Please Choose Another One")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# form for request user toe nter email for reset
class ResetRequest(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Request Email Reset")

    # validate password
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
    title = StringField("Title",validators=[DataRequired()])
    category = SelectField("Cetegory",validators=[DataRequired()])
    price = StringField("Price",validators=[DataRequired()])
    media = FileField("Images/Videos",validators=[DataRequired(),FileAllowed(["jpg", "png","mp4","mkv"])])
    description = TextAreaField("Description",validators=[DataRequired()])
    expires = StringField("When Post Expires",validators=[DataRequired()])
    active = RadioField("Active",choices=["Active","Not Active"])
    submit = SubmitField("Save The product")

    # validate password
    def validate_product(self, title):
        product = Product.query.filter_by(name=title.data).first()
        if product is not None:
            flash("Product With that name Exists. Please Use another name","warning")


class CategoryForm(FlaskForm):
    name = StringField("name",validators=[DataRequired()])
    submit = SubmitField("Save Category")


    def validate_category(self,name):
        category = Category.query.filter_by(name=name.data).first()

        if category is not None:
            flash("Category Name Already Exists.","warning")


