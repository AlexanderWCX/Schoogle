# import relevant stuff
# all imported modules must be placed in python34/lib/site-packages or it will not be found
from flask import Flask, render_template, url_for, request, redirect, flash
from flaskForm import RegistrationForm, LoginForm
from newUser import writeNewUserToDB

# create a flask object
app = Flask(__name__)

# set the secret key for the app for security reasons
app.config['SECRET_KEY'] = 'carol98hanee96alex96germ98'

# route to login page
@app.route('/login')
def login():
	return render_template('login.html')

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
	


# run the app
if __name__ == '__main__':
    app.run(debug=True)

