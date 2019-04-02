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
from saveRemoveSchool import saveSchool, deleteSavedSchool
from wtforms import StringField, PasswordField, SubmitField, BooleanField, widgets, SelectMultipleField
import globalvariables
import globalupdater
from sortingAndRelatedFunctions import getMap, retrieveSavedSchools, sortByAlphabetical, sortByDistance, sortBySavedDate, retrievePostalCode
from schoolInfoFetching import website, generalInformation, subjectsOffered, physicalCCAs, artsCCAs, clubCCAs, uniformCCAs, contactInfo, gettingThere
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
		#print('setting global variable successful')
		#print(global_list_of_schools)

		global global_email
		if global_email == "NIL":
			return redirect(url_for('results'))
		
		else:
			return redirect(url_for('loggedinresults'))
		
	# with the form object and html template, render the template and return it to route 	
	return render_template('searchByN.html', form = form)

@app.route('/savedlist', methods=['get', 'post'])
def savedlist():

	global global_email
	if global_email == "NIL":
		return redirect(url_for('notloggedin'))
	
	hasPostalCode = True

	global userPostalCode
	userPostalCode = retrievePostalCode(global_email)
	if userPostalCode == "null":
		hasPostalCode = False

	global global_userSavedSchoolList
	#global_userSavedSchoolList = retrieveSavedSchools(global_email)
	schoolList = global_userSavedSchoolList
	#print(global_userSavedSchoolList)

	if request.method == 'POST':

		list = request.form
		#print(list)
		keys = list.keys()

		schoolToUnsaveList = request.form.getlist('unsaveList')
		#print(schoolToUnsaveList)
		if schoolToUnsaveList:
			for school in schoolToUnsaveList:
				unsaveStatus = deleteSavedSchool(global_email, school)
				#print(unsaveStatus)

			return redirect(url_for('savedlist'))

		elif keys:

			alphabetical = "alphabetical"
			distance = "distance"
			savedDate = "saveddate"

			if alphabetical in list:
				global_userSavedSchoolList = sortByAlphabetical(schoolList)
				#print(global_userSavedSchoolList)
				return redirect(url_for('savedlist'))

			elif distance in list:
				sortedList = sortByDistance(global_userSavedSchoolList, userPostalCode)
				global_userSavedSchoolList =sortedList[0]
				
				#print(schoolList)
				return redirect(url_for('savedlist'))
			
			elif savedDate in list:
				global_userSavedSchoolList = sortBySavedDate(global_email)
				#print(schoolList)
				return redirect(url_for('savedlist'))

			else:

				for key in keys:
					school = key
				
				#print(school)

				global clickedschool
				clickedschool = school

				return redirect(url_for('schoolinfo', clickedschool = clickedschool))


	return(render_template('usersavedlist.html', global_userSavedSchoolList = global_userSavedSchoolList, hasPostalCode = hasPostalCode))


@app.route('/notloggedin')
def notloggedin():
	return(render_template('notloggedin.html'))

@app.route('/results', methods=['get', 'post'])
def results():

	global global_list_of_schools
	schoolList = global_list_of_schools
	#print('im in results route')
	
	if request.method == 'POST':
		list = request.form
		#print(list)
		keys = list.keys()
		#print(keys)
		
		alphabetical = "alphabetical"

		if alphabetical in list:
			global_list_of_schools = sortByAlphabetical(schoolList)
			#print(schoolList)
			return redirect(url_for('results'))

		else:
			for key in keys:
				#print(key)
				school = key
				#print(school)

				global clickedschool
				clickedschool = school

				return redirect(url_for('schoolinfo', global_list_of_schools= global_list_of_schools))
		
	return render_template('results.html', schoolList = schoolList)
			

@app.route('/loggedinresults', methods=['get', 'post'])
def loggedinresults():

	global global_list_of_schools
	schoolList = global_list_of_schools

	global global_email
	usersemail = global_email

	hasPostalCode = True

	global userPostalCode
	userPostalCode = retrievePostalCode(global_email)
	if userPostalCode == "null":
		hasPostalCode = False

	userSavedList = retrieveSavedSchools(global_email)
	

	if request.method == 'POST':
		
		list = request.form
		#print(list)
		keys = list.keys()
		
		schoolToSaveList = request.form.getlist('schooloptions')
		#print(schoolToSaveList)

		if schoolToSaveList:
			for school in schoolToSaveList:
				now = datetime.now()
				#print(now)
				savestatus = saveSchool(usersemail, school, now)
				#print(savestatus)

			return redirect(url_for('loggedinresults'))

		elif keys:

			alphabetical = "alphabetical"
			distance = "distance"

			if alphabetical in list:
				global_list_of_schools = sortByAlphabetical(schoolList)
				#print(schoolList)
				return redirect(url_for('loggedinresults'))

			elif distance in list:
				sortedList = sortByDistance(global_list_of_schools, userPostalCode)
				global_list_of_schools =sortedList[0]
				
				#print(schoolList)
				return redirect(url_for('loggedinresults'))

			else:
				for key in keys:
					
					school = key
				
					print(school)

					global clickedschool
					clickedschool = school

					return redirect(url_for('schoolinfo', clickedschool=clickedschool))

	return render_template('loggedinresults.html', global_list_of_schools = global_list_of_schools, userSavedList= userSavedList, hasPostalCode=hasPostalCode)

@app.route('/schoolinfo')
def schoolinfo():

	global clickedschool

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
		
	
	email = schoolcontactInfo[0]
	telephone = schoolcontactInfo[1]
	fax = schoolcontactInfo[2]
		
	
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

