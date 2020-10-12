# import relevant stuff
# all imported modules must be placed in python34/lib/site-packages or it will not be found
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, widgets, SelectMultipleField
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


class LoginForm(FlaskForm):

    email = StringField('Email:', validators = [DataRequired(), Email()])

    # if password is not found in userInformation database, it is wrong
    # no need for security checks
    password = PasswordField('Password:', validators = [DataRequired()])

    submit = SubmitField('Log In!')


# create a class named SearchByNForm
class SearchByNForm(FlaskForm):

	# forms use objects to handle user input 

    # keyword is a required field 
    keyword = StringField('Search:', validators = [DataRequired()]) 

    # create a submit object
    submit = SubmitField('Submit!')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SearchByCForm(FlaskForm):
    
    list_of_sports = ['Adventure Club', 'Air Rifle/Shooting', 'Artistics Gymnastics', 'Athletics', 'Badminton', 'BasketBall', 'Cricket', 'Cross Country', 'Fencing', 'Floorball', 'Football', 'Frisbee', 'Golf', 'Hockey', 'Judo', 'Karate', 'Rhythmic Gymnastics', 'Rugby', 'Sailing', 'Sepak Takraw', 'Softball', 'Squash', 'Swimming', 'Table Tennis', 'Taekwondo', 'Tchoukball', 'Ten-pin Bowling', 'Tennis', 'Track & Field', 'Trampoline', 'Volleyball', 'Wushu']
    #create a list of value/description tuples
    sportschoices = [(x, x) for x in list_of_sports]
    sports = MultiCheckboxField('Physical Sports', choices=sportschoices)

    list_of_societies = ['Aero-Modelling', 'Astronomy Club', 'Audio & Video/ PA Club', 'Audio Video and Information Technology Club', 'Chess Club', 'Chinese Society', 'Computer Club', 'Green Club', 'Infocom Club', 'IT Club', 'Japanese Club', 'Photographic Society', 'Robotics Club', 'Scrabble Club', 'Service Learning Club']
    #create a list of value/description tuples
    societieschoices = [(x, x) for x in list_of_societies]
    societies = MultiCheckboxField('Clubs & Societies', choices=societieschoices)

    list_of_uniformed = ["Boys' Brigade", 'Girl Guides', "Girls' Brigade", 'National Civil Defence Cadet Corps', 'NCC (Land)', 'NCC(Sea', 'NCC(Air)', 'NPCC', 'NPCC(Sea)', 'Scouts', "St. John Brigade", "Singapore Red Cross Society"]
    #create a list of value/description tuples
    uniformedchoices = [(x, x) for x in list_of_uniformed]
    uniformed = MultiCheckboxField('Uniformed Groups', choices=uniformedchoices)

    list_of_arts = ['Art & Craft Club', 'Arts and Innovation Club', 'Arts Society', 'Band - Concert', 'Band - Display/Marching', 'Band - Military', 'Band - Pipe', 'Band - Symphonic', 'Choir', 'Dance - Ballet', 'Dance - Chinese', 'Dance - Indian', 'Dance - International', 'Dance - Malay', 'Dance - Modern', 'Drama - Chinese', 'Drama - English', 'Drama - Tamil', 'Ensemble - Guitar', 'Ensemble - Guzheng', 'Ensemble - Harmonica', 'Ensemble - Percussion', 'Ensemble - String', 'Lion Dance Troupe', 'Orchestra - Chinese', 'Orchestra - Indian']
    #create a list of value/description tuples
    artschoices = [(x, x) for x in list_of_arts]
    arts = MultiCheckboxField('Visual & Performing Arts', choices=artschoices)

    list_of_others = ['Prefectorial Board', "Students' Council", 'House Appointment']
    #create a list of value/description tuples
    otherschoices = [(x, x) for x in list_of_others]
    others = MultiCheckboxField('Others', choices=otherschoices)

    list_of_subjects = ["Art 'O' Level", 'Combined Humanities (S,G)', 'Combined Humanities (S,H)', 'Combined Humanities (S,L)', 'Computer Applications', 'Drama', 'Elements of Business Skills', 'Exercise and Sports Science', 'Food & Nutrition', 'Geography', 'History', 'Mobile Robotics', "Music 'O' Level", "Physical Education", 'Principle of Accounts', 'Science (Chem, Bio)', 'Science (Phy, Bio)', 'Science (Phy, Chem)', 'Chemistry', 'Physics', 'Biology', 'Chinese', 'Malay', 'Tamil']
    #create a list of value/description tuples
    subjectschoices = [(x, x) for x in list_of_subjects]
    subjects = MultiCheckboxField('Subjects', choices=subjectschoices)

    list_of_types = ['Government School', 'Government-Aided School', 'Independent School', 'Specialised School', 'Specialised Independent School']
    #create a list of value/description tuples
    typeschoices = [(x, x) for x in list_of_types]
    types = MultiCheckboxField('Type of School', choices=typeschoices)

    list_of_gender = ["Boys' School", "Girls' School", 'Co-ed School']
    #create a list of value/description tuples
    genderchoices = [(x, x) for x in list_of_gender]
    gender = MultiCheckboxField('Gender of Students', choices=genderchoices)

    list_of_focus = ['STEM', 'Languages & Humanities', 'Business & Entrepreneurship', 'Aesthetics', 'Humanities', 'Languages']
    #create a list of value/description tuples
    focuschoices = [(x, x) for x in list_of_focus]
    focus = MultiCheckboxField('Distinctive Programmes', choices=focuschoices)

    # create a submit object
    submit = SubmitField('Submit!')




    

    
