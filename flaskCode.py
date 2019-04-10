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
from saveRemoveSchool import saveSchool, deleteSavedSchool
from wtforms import StringField, PasswordField, SubmitField, BooleanField, widgets, SelectMultipleField
from sortingAndRelatedFunctions import retrieveSavedSchools, sortByAlphabetical, sortByDistance, sortBySavedDate, retrievePostalCode
from schoolInfoFetching import getMap, website, generalInformation, subjectsOffered, physicalCCAs, artsCCAs, clubCCAs, uniformCCAs, contactInfo, gettingThere
from datetime import datetime

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
global clickedschool
clickedschool = "NO SCHOOL SELECTED"
global userPostalCode
userPostalCode = 0
global global_userSavedSchoolList
global_userSavedSchoolList = []

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
				global global_userSavedSchoolList
				global_userSavedSchoolList = retrieveSavedSchools(global_email)
				# both email and password are correct, redirect to initial UI page
				return redirect(url_for('savedlist'))


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
		

		# get list of visual & performing arts CCAs that was selected
		arts = form.arts.data
		

		# get list of uniformed group CCAs that was selected
		uniformed = form.uniformed.data
		

		# get list of clubs & societies CCAs that was selected
		societies = form.societies.data
		

		# get list of others CCAs that was selected
		others = form.others.data
		
		
		#prepare lists to feed into searchByC function
		ccaList = sports + arts + uniformed + societies + others
		subjectList = form.subjects.data
		typeList = form.types.data
		genderList = form.gender.data
		focusList = form.focus.data

		#get final list of schools that match all criterias
		resultslist = searchByC(ccaList, subjectList, typeList, genderList, focusList)
		
		#set global list of schools variable to the resultant list of schools
		global global_list_of_schools
		global_list_of_schools = resultslist

		#get global email
		global global_email

		#redirect to normal results page if not logged in
		if global_email == "NIL":
			return redirect(url_for('results'))
		
		#redirect to logged in results page if logged in
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

		#input keyword into searchByN function to get list of schools containing the keyword
		resultslist = searchByN(keyword)
		global_list_of_schools = resultslist

		#get global email
		global global_email

		#redirect to normal results page if not logged in
		if global_email == "NIL":
			return redirect(url_for('results'))
		
		#redirect to logged in results page if logged in
		else:
			return redirect(url_for('loggedinresults'))
		
	# with the form object and html template, render the template and return it to route 	
	return render_template('searchByN.html', form = form)

@app.route('/savedlist', methods=['get', 'post'])
def savedlist():

	#get global email
	global global_email

	#redirect to error page if not logged in
	if global_email == "NIL":
		return redirect(url_for('notloggedin'))
	
	#set hasPostalCode variable to a have a default value of True
	hasPostalCode = True

	#get global userPostalCode
	global userPostalCode
	userPostalCode = retrievePostalCode(global_email)

	#if registered user did not register their postal code, set hasPostalCode to false
	if userPostalCode == "null":
		hasPostalCode = False

	#get user's list of saved schools
	global global_userSavedSchoolList
	schoolList = global_userSavedSchoolList
	
	#in the event of any POST method
	if request.method == 'POST':

		#get list of keys from the form
		list = request.form
		keys = list.keys()

		#get list of schools to unsave from the form
		schoolToUnsaveList = request.form.getlist('unsaveList')
		
		#if user has selected any schools to unsave
		if schoolToUnsaveList:
			
			#unsave all selected schools
			for school in schoolToUnsaveList:
				unsaveStatus = deleteSavedSchool(global_email, school)
			
			global_userSavedSchoolList = retrieveSavedSchools(global_email)

			#redirect back to savedlist page after unsaving is successful
			return redirect(url_for('savedlist'))

		#else if the list of keys from the form is not empty
		elif keys:

			alphabetical = "alphabetical"
			distance = "distance"
			savedDate = "saveddate"

			#if the key named 'alphabetical' is in the list
			if alphabetical in list:
				
				#sort list of schools alphabetically
				global_userSavedSchoolList = sortByAlphabetical(schoolList)
				
				#redirect to savedlist page
				return redirect(url_for('savedlist'))

			#if the key named 'distance' is in the list
			elif distance in list:

				#sort list of schools in terms of increasing distance
				sortedList = sortByDistance(global_userSavedSchoolList, userPostalCode)
				
				#get sorted list of schools
				global_userSavedSchoolList =sortedList[0]
				
				#redirect to savedlist page
				return redirect(url_for('savedlist'))
			
			#if the key named 'savedDate' is in the list
			elif savedDate in list:

				#sort list of schools in terms of saved date
				sortedList = sortBySavedDate(global_email)

				#get list of sorted schools
				global_userSavedSchoolList =sortedList[0]
				
				#redirect to savedlist page
				return redirect(url_for('savedlist'))

			#if 'more information' button is clicked
			else:
				
				#get school that user clicked on
				for key in keys:
					school = key
				
				global clickedschool
				clickedschool = school

				#redirect to schoolinfo of clicked school
				return redirect(url_for('schoolinfo', clickedschool = clickedschool))


	return(render_template('usersavedlist.html', global_userSavedSchoolList = global_userSavedSchoolList, hasPostalCode = hasPostalCode))


@app.route('/notloggedin')
def notloggedin():
	return(render_template('notloggedin.html'))

@app.route('/results', methods=['get', 'post'])
def results():

	#get list of schools to display
	global global_list_of_schools
	schoolList = global_list_of_schools
	
	#in the event of any POST method
	if request.method == 'POST':
		
		#get list of keys from the form
		list = request.form
		keys = list.keys()
		
		alphabetical = "alphabetical"

		#if the key named 'alphabetical' is in the list
		if alphabetical in list:
			
			#sort list of schools alphabetically
			global_list_of_schools = sortByAlphabetical(schoolList)
			
			#redirect to savedlist page
			return redirect(url_for('results'))

		#if 'more information' button is clicked
		else:
			
			#get school that user clicked on
			for key in keys:
				school = key
			
			global clickedschool
			clickedschool = school

			#redirect to schoolinfo of clicked school
			return redirect(url_for('schoolinfo', global_list_of_schools= global_list_of_schools))
		
	return render_template('results.html', schoolList = schoolList)
			

@app.route('/loggedinresults', methods=['get', 'post'])
def loggedinresults():

	#get list of schools to display
	global global_list_of_schools
	schoolList = global_list_of_schools

	#get email of logged in user
	global global_email
	usersemail = global_email

	#set hasPostalCode variable to a have a default value of True
	hasPostalCode = True

	#get global userPostalCode
	global userPostalCode
	userPostalCode = retrievePostalCode(global_email)

	#if registered user did not register their postal code, set hasPostalCode to false
	if userPostalCode == "null":
		hasPostalCode = False

	#get list of schools saved by the user
	userSavedList = retrieveSavedSchools(global_email)
	
	#in the event of any POST method
	if request.method == 'POST':
		
		#get list of keys from the form
		list = request.form
		keys = list.keys()
		
		#get list of selected schools the user wishes to save
		schoolToSaveList = request.form.getlist('schooloptions')
		
		#if user has selected any schools to save
		if schoolToSaveList:
			
			#save all selected schools
			for school in schoolToSaveList:
				
				now = datetime.now()
				savestatus = saveSchool(usersemail, school, now)

			global global_userSavedSchoolList
			global_userSavedSchoolList = retrieveSavedSchools(global_email)
					
			#redirect to resuts page
			return redirect(url_for('loggedinresults'))

		#else if the list of keys from the form is not empty
		elif keys:
			
			alphabetical = "alphabetical"
			distance = "distance"

			#if the key named 'alphabetical' is in the list
			if alphabetical in list:
				
				#sort list of schools alphabetically
				global_list_of_schools = sortByAlphabetical(schoolList)
				
				#redirect to savedlist page
				return redirect(url_for('loggedinresults'))

			#if the key named 'distance' is in the list
			elif distance in list:

				#sort list of schools by increasing distance
				sortedList = sortByDistance(global_list_of_schools, userPostalCode)
				
				#get list of sorted schools
				global_list_of_schools =sortedList[0]
				
				#redirect to savedlist page
				return redirect(url_for('loggedinresults'))

			#if 'more information' button is clicked
			else:

				#get school that user clicked on
				for key in keys:
					
					school = key

				global clickedschool
				clickedschool = school
				
				#redirect to schoolinfo of clicked school
				return redirect(url_for('schoolinfo', clickedschool=clickedschool))

	return render_template('loggedinresults.html', global_list_of_schools = global_list_of_schools, userSavedList= userSavedList, hasPostalCode=hasPostalCode)

@app.route('/schoolinfo')
def schoolinfo():

	#get name of clicked school
	global clickedschool

	#create map of clicked school
	url = getMap(clickedschool)

	# Getting information from databases
	schoolwebsite = website(clickedschool)
	schoolgeneralInfoList = generalInformation(clickedschool)
	subjectList = subjectsOffered(clickedschool)
	schoolphysicalCCAs = physicalCCAs(clickedschool)
	schoolartsCCAs = artsCCAs(clickedschool)
	schoolclubCCAs = clubCCAs(clickedschool)
	schooluniformCCAs = uniformCCAs(clickedschool)
	schoolcontactInfo = contactInfo(clickedschool)
	schoolgettingThere = gettingThere(clickedschool)

	if schoolwebsite == "None":
		schoolwebsite = "No website found"

	if not schoolgeneralInfoList:
		for x in range(0, 6):
			message = "No information found"
			schoolgeneralInfoList.append(message)

	#getting individual info from general information list
	schooltype = schoolgeneralInfoList[0]
	schooltype.title()
	gender = schoolgeneralInfoList[1]
	gender.title()
	principal = schoolgeneralInfoList[2]
	principal.title()
	vision = schoolgeneralInfoList[3]
	mission = schoolgeneralInfoList[4]
	philosophy = schoolgeneralInfoList[5]
	
					
	if not subjectList:
		message = "No information found"
		subjectList.append(message)

	if not schoolphysicalCCAs:
		message = "No information found"
		schoolphysicalCCAs.append(message)
	
	if not schoolartsCCAs:
		message = "No information found"
		schoolartsCCAs.append(message)
	
	if not schoolclubCCAs:
		message = "No information found"
		schoolclubCCAs.append(message)
	
	if not schooluniformCCAs:
		message = "No information found"
		schooluniformCCAs.append(message)
		
	#getting individual info from contact info list
	email = schoolcontactInfo[0]
	telephone = schoolcontactInfo[1]
	fax = schoolcontactInfo[2]
		
	#getting individual info from getting there list
	address = schoolgettingThere[0]
	postalcode = schoolgettingThere[1]
	nearestMRT = schoolgettingThere[2]
	buses = schoolgettingThere[3]


	return(render_template('schoolinfo.html', clickedschool = clickedschool, schoolwebsite = schoolwebsite,
    schooltype = schooltype, gender = gender, principal = principal, vision = vision, mission = mission, philosophy = philosophy, 
	subjectList = subjectList, schoolphysicalCCAs = schoolphysicalCCAs, schoolartsCCAs = schoolartsCCAs, 
	schoolclubCCAs = schoolclubCCAs, schooluniformCCAs = schooluniformCCAs,
	email = email, telephone = telephone, fax = fax, address = address,
	postalcode = postalcode, nearestMRT = nearestMRT, buses = buses, url = url ))





# run the app
if __name__ == '__main__':
    app.run(debug=True)

