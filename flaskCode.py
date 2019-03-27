# import relevant stuff
# all imported modules must be placed in python34/lib/site-packages or it will not be found
from flask import Flask, render_template, url_for, request, redirect, flash
from flaskForm import RegistrationForm, LoginForm, SearchByNForm, SearchByCForm
from wtforms import SelectMultipleField
from flask_wtf import FlaskForm
from newUser import writeNewUserToDB
from verifyEmailAndPassword import findEmailInDB, passwordMatchesThatPairedWithEmailInDB 
from searchByN import searchByN
from searchByC import searchByC
from saveRemoveSchool import saveSchool
from wtforms import StringField, PasswordField, SubmitField, BooleanField, widgets, SelectMultipleField
import globalvariables
import globalupdater

# create a flask object
app = Flask(__name__)

# set the secret key for the app for security reasons
app.config['SECRET_KEY'] = 'carol98hanee96alex96germ98'
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

#create global variables that 
log_in = False 
global_email = "none"
global_list_of_schools = []

@app.route('/')
@app.route('/home')
def home():
	return(render_template('initialUI.html'))

# route to login page
@app.route('/login', methods = ['get', 'post'])
def login():

	# create the form object
	form = LoginForm()

	# validate user input
	if form.validate_on_submit():
		# all form data is stored in the request object flask auto creates
		# read in the email
		email = request.form['email']

		# returns the row index the email is located in in the userInformation database, if found
		emailRow = findEmailInDB(email)

		# an actual row index got returned
		if emailRow > 0:
			# read in the password
			password = request.form['password']

			# make sure that the password matches that paired with that email in database
			matches = passwordMatchesThatPairedWithEmailInDB(password, emailRow)
			if matches == True:
				globalupdater.update_log_in(True)
				globalupdater.update_global_email(email)
				# both email and password are correct, redirect to initial UI page
				return redirect(url_for('home'))


	# render template on html and form
	return render_template('login.html', form = form)

# route to sign up page
# route has to accept get and post requests
@app.route('/signup', methods=['get', 'post'])
# include the function below in the above route method using @
def signUp():
	
	# create the form object
	form = RegistrationForm()

	# read in the user input data only if they have all passed validation checks
	if form.validate_on_submit():

		# the user input data will be found in the request object that flask automatically creates

		# extract the email
		email = request.form['email']

		# extract the password
		password = request.form['password']

		# extract the postal code
		postalCode = request.form['postalCode']

		# call the method to write email, password and postal code to the userInformation database
		written = writeNewUserToDB(email, password, postalCode)

		# if written is true, redirect to the login page
		if written == True:
			return redirect(url_for('login'))


	# with the form object and html template, render the template and return it to route 
	return render_template('signupform.html', form = form)
	
	
@app.route('/search')
def search():
	return(render_template('searchhome.html'))

@app.route('/searchbyc', methods=['get', 'post'])
def searchByCpage():
	form = SearchByCForm()

	# read in the user input data only if they have passed validation checks
	if form.validate_on_submit():
		# get list of sports CCAs that was selected
		sports = form.sports.data
		#print(sports)

		# get list of visual & performing arts CCAs that was selected
		arts = form.arts.data
		#print(arts)

		# get list of uniformed group CCAs that was selected
		uniformed = form.uniformed.data
		#print(uniformed)

		# get list of clubs & societies CCAs that was selected
		societies = form.societies.data
		#print(societies)

		# get list of others CCAs that was selected
		others = form.others.data
		#print(others)
		
		#prepare lists to feed into searchByC function
		ccaList = sports + arts + uniformed + societies + others
		subjectList = form.subjects.data
		typeList = form.types.data
		genderList = form.gender.data
		focusList = form.focus.data
	
		resultslist = searchByC(ccaList, subjectList, typeList, genderList, focusList)
		globalupdater.update_school_list(resultslist)

		return render_template('results.html', resultslist=resultslist)

	# with the form object and html template, render the template and return it to route 	
	return render_template('searchByC.html', form = form)

@app.route('/searchbym')
def searchByM():
	return(render_template('searchbyM.html'))

@app.route('/searchbyn', methods=['get', 'post'])
def searchByNpage():
	# create the form object
	form = SearchByNForm()

	# make sure the form validates upon user submission and capture the boolean
	if form.validate_on_submit():
		
		global global_list_of_schools

		# the user input data will be found in the request object that flask automatically creates
		keyword = request.form['keyword']
		resultslist = searchByN(keyword)
		globalupdater.update_school_list(resultslist)

		#print(resultslist)
		print('setting global variable successful')
		print(resultslist)
		
		return redirect(url_for('results'))
		
	# with the form object and html template, render the template and return it to route 	
	return render_template('searchByN.html', form = form)

@app.route('/savedlist')
def savedlist():
	return(render_template('usersavedlist.html'))

@app.route('/results')
def results():

	form = SaveSchoolsForm()
	print('im at form=SaveSchoolsForm at flaskCode')


	if True:
		
		#get list of schools chosen to be saved
		schoolResultsList = form.schools.data
		print('gotten schoolResultsList')
		print(schoolResultsList)

		#checking if the user has logged in
		usersemail = globalvariables.global_email 
		if usersemail == "NIL":
			print("you have not logged in")
			flash("you have not logged in")
		
		#iterate through the list of schools and save them all
		else: 
			for school in schoolResultsList:
				saveSchool(usersemail, school, 100)
				print("its saved")


	return render_template('results.html', form=form)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SaveSchoolsForm(FlaskForm):

    resultslist = globalvariables.school_list
    print('im reading at saveschoolsform')
    print(resultslist)
    schoolchoices = [(x, x) for x in resultslist]
    schools = MultiCheckboxField('Results', choices=schoolchoices)

    



	









# run the app
if __name__ == '__main__':
    app.run(debug=True)

