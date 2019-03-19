# import relevant stuff
# all imported modules must be placed in python34/lib/site-packages or it will not be found
from flask import Flask, render_template, url_for, request
from flaskForm import RegistrationForm, LoginForm

# create a flask object
app = Flask(__name__)

# set the secret key for the app for security reasons
app.config['SECRET_KEY'] = 'carol98hanee96alex96germ98'

# route to sign up page
# route has to accept get and post requests
@app.route('/signup', methods=['get', 'post'])
# include the function below in the above route method using @
def signUp():
	
	# create the form object
	form = RegistrationForm()
	
	# make sure the form validates upon user submission and capture the boolean
	validated = form.validate_on_submit()
	
	# try to read in the user input data
	try:
		# read in the user input data only if they have passed validation checks
		if validated == True:
			# the user input data will be found in the request object that flask automatically creates
			email = request.form['email']
			print(email)
	
	# if the user has not submitted anything, do nothing for now
	except:
		None 
	
	# with the form object and html template, render the template and return it to route 
	return render_template('signupform.html', form = form)
	



# run the app
if __name__ == '__main__':
    app.run(debug=True)

