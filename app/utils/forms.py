from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, EmailField, IntegerField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models.User import User


class RegisterForm(FlaskForm):

    username = StringField(label="User Name:", validators=[Length(min=3, max=30), DataRequired()])
    email = EmailField(label="Email Address:", validators=[Email(message='Not a valid email address.'), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired(message="Please enter a password.")])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo("password1", message='Passwords must match.'), DataRequired(message="Please Re-enter password.")])
    submit = SubmitField(label="Create Account")

    def validate_username(self, in_usr):
        user = User.query.filter_by(usrname=in_usr.data).first()
        if user:
            raise ValidationError("Username already taken")

    def validate_email(self, in_mail):
        email = User.query.filter_by(usrmail=in_mail.data).first()
        if email:
            raise ValidationError("Email Address already exists for an account")


class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item!")

class PriceChangeForm(FlaskForm):
    price = IntegerField(label="New Item Price in Dollars:", validators=[DataRequired()])
    submit = SubmitField(label="Confirm Price Change")

class PostItemForm(FlaskForm):
    itmname = StringField(label="Item Name:", validators=[Length(min=3, max=30), DataRequired()])
    price = IntegerField(label="Item Price in Dollars:", validators=[DataRequired()])
    barcode = StringField(label="Item Barcode:", validators=[Length(min=12, max=12)])
    description = TextAreaField(label="Item Description:")
    submit = SubmitField(label="Post Item")