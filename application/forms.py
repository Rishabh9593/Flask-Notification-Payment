from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
#from wtforms.fields import Field
from application.models import User

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


'''
class AdminRegisterForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
         # pylint: disable=no-member
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")
'''
class RegisterForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    Year = StringField("Year", validators=[DataRequired(),Length(min=2,max=55)])
    branch = StringField("Branch", validators=[DataRequired(),Length(min=2,max=55)])
    TelegramUserID = StringField("Telegram User ID (get from @userinfobot)", validators=[DataRequired(),Length(min=9,max=12)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
         # pylint: disable=no-member
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")
'''
class StaffRegisterForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
         # pylint: disable=no-member
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

'''


    