from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class NewProductRequestForm(Form):
    productName = StringField('Product Name', validators=[DataRequired("Please enter the data.")])
    region = StringField('Region', validators=[DataRequired("Please enter the data.")])
    technology = StringField('Technology', validators=[DataRequired("Please enter the data.")])
    usersCategory = StringField('Users Category', validators=[DataRequired("Please enter the data.")])
    environment = StringField('Environment', validators=[DataRequired("Please enter the data.")])
    serviceCodeType = StringField('Service Code/Type', validators=[DataRequired("Please enter the data.")])
    dpiParameters = StringField('DPI Parameters', validators=[DataRequired("Please enter the data.")])
    policyName = StringField('Policy Name', validators=[DataRequired("Please enter the data.")])
    submit = SubmitField("Submit Request")
