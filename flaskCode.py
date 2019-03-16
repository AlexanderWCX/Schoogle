#remember to copy this file and the templates folder to desktop or flask will not be found

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def printSomething():
    return render_template('initialUI.html')

if __name__=='__main__':
    app.run(debug=True)

