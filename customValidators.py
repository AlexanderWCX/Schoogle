# a copy of this code is found in python34/lib/site-packages, so that it can be imported

# import relevant stuff
from wtforms.validators import ValidationError

# define a class to be a custom validator not found in wtforms.validators
# PasswordSecurity inherits from object
class PasswordSecurity(object):

    # initialize class
    def __init__(self, message=None):

        # message will be referenced later at raise validation error
        self.message = message

    # define a __call__ method to perform the validation 
    def __call__(self, form, field):

        # set the error message
        message = 'Password does not fulfil the requirements. Please try again!'

        # if password does not contain exactly 1 capital letter and exactly 1 number, raise error message

        # initialize countCapitalLetters to 0
        countCapitalLetters = 0

        # initialize countNumbers to 0
        countNumbers = 0

        # loop through each character in password
        for char in field.data:
            # if the character is a capital letter, increment countCapitalLetters
            if char.isupper():
                countCapitalLetters += 1

            # if the character is a number, increment countNumbers
            elif char.isdigit():
                countNumbers += 1

        # if both counts are not exactly 1, raise error
        if ((countCapitalLetters != 1) or (countNumbers != 1)):
            raise ValidationError(message)
