# import relevant stuff
# all imported modules must be placed in python34/lib/site-packages or it will not be found
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional
from customValidators import PasswordSecurity

# create a class named RegistrationForm
class RegistrationForm(FlaskForm):

	# forms use objects to handle user input 

    # create an email object
    # email is a required field and must be a valid address
    email = StringField('Email:', validators = [DataRequired(), Email()])

    # create a password object
    # password is a required field, has a certain length, and must pass security requirements 
    password = PasswordField('Password:', validators = [DataRequired(), Length(min = 8, max = 12), PasswordSecurity()])

    # create a confirm password object
    # confirmPassword is a required field and must be equal to password
    confirmPassword = PasswordField('Re-enter Password:', validators = [DataRequired(), EqualTo('password')])

    # create a postal code object
    # postal code is an optional field and must be 6 digits
    postalCode = StringField('Postal Code: (optional)', validators = [Optional(), Length(min = 6, max = 6)])

    # create a submit object
    submit = SubmitField('Sign Up!')

# create a class named LoginForm
class LoginForm(FlaskForm):

	# forms use objects to handle user input 

    # create an email object
    # email is a required field and must be a valid address
    email = StringField('Email:', validators = [DataRequired(), Email()])

    # create a password object
    # password is a required field
    password = PasswordField('Password:', validators = [DataRequired()])

    # create a submit object
    submit = SubmitField('Log In!')
