# import relevant stuff
# all modules must be placed in python34/lib/site-packages or it will not be found
from flask import Flask, render_template, url_for
from flaskForm import RegistrationForm, LoginForm

# create a flask object
app = Flask(__name__)

# set the secret key for the app for security reasons
app.config['SECRET_KEY'] = 'carol98hanee96alex96germ98'

# route to sign up page
@app.route('/signupform')
# include the function below in the above route method using @
def signUp():

    # create the form object
    form = RegistrationForm()

    #render the html template and return it
    return render_template('signupform.html', form=form)



# run the app
if __name__ == '__main__':
    app.run(debug=True)

