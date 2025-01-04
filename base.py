from flask import Flask,redirect,render_template,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,RadioField, BooleanField

app = Flask(__name__)



############
#forms#

class drone(FlaskForm):
    amount = IntegerField("How Many Drones do you Have? ")
    whatType = RadioField("What types do you Fly? ",choices=[("fpv","FPV"),("Compat","Compact Portable"),("both","Both")])
    better = BooleanField("which one do you prefer? ",choices=[("fpv","FPV"),("Compat","Compact Portable")])
    fav = StringField("Favorite drone you have: ")
    submit = SubmitField("Submit")
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/mydrones')
def mydrones():
    return render_template("mydrones.html")

@app.route('/yourdrones')
def yourdrones():
    return render_template("urdrone.html")

@app.route('/results')
def results():
    return render_template("cooldrone.html")

if __name__ == '__main__':
    app.run(debug=True)