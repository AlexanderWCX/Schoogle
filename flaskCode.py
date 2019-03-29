# import relevant stuff
# all imported modules must be placed in python34/lib/site-packages or it will not be found
from flask import Flask, render_template, url_for, request, redirect, flash
from flaskForm import RegistrationForm, LoginForm, SearchByNForm, SearchByCForm, SaveSchoolsForm
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


#create global variables that 
global log_in 
log_in = False 
global global_email 
global_email = "NIL"
global global_list_of_schools 
global_list_of_schools = []
global usersavedschool
usersavedschool =[]

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
				global log_in
				log_in = True
				global global_email
				global_email = email
				# both email and password are correct, redirect to initial UI page
				return redirect(url_for('search'))


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
		global global_list_of_schools
		global_list_of_schools = resultslist

		global global_email
		if global_email == "NIL":
			return redirect(url_for('results'))
		
		else:
			return redirect(url_for('loggedinresults'))

		

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
		global_list_of_schools = resultslist

		#print(resultslist)
		print('setting global variable successful')
		#print(global_list_of_schools)

		global global_email
		if global_email == "NIL":
			return redirect(url_for('results'))
		
		else:
			return redirect(url_for('loggedinresults'))
		
	# with the form object and html template, render the template and return it to route 	
	return render_template('searchByN.html', form = form)

@app.route('/savedlist')
def savedlist():
	return(render_template('usersavedlist.html'))

@app.route('/results', methods=['get', 'post'])
def results():

	global global_list_of_schools
	#print('im in results route')	
		
	return render_template('results.html', global_list_of_schools = global_list_of_schools)
			

@app.route('/loggedinresults', methods=['get', 'post'])
def loggedinresults():

	global global_list_of_schools

	global global_email
	usersemail = global_email

	if request.method == 'POST':
		schoolToSaveList = request.form.getlist('schooloptions')
		#print(schoolToSaveList)

		for school in schoolToSaveList:
				savestatus = saveSchool(usersemail, school, 100)
				#print(savestatus)

		return redirect(url_for('loggedinresults'))

	return render_template('loggedinresults.html', global_list_of_schools = global_list_of_schools)

@app.route('/css')
def css():
	return(render_template('bootstrap_def.css'))





	









# run the app
if __name__ == '__main__':
    app.run(debug=True)

