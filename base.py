from flask import Flask,redirect,render_template,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,RadioField, BooleanField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

############
#forms#

class drone(FlaskForm):
    amount = IntegerField("How Many Drones do you Have? ")
    whatType = RadioField("What types do you Fly? ",choices=[("fpv","FPV"),("Compat","Compact Portable"),("both","Both")])
    better = RadioField("which one do you prefer? ",choices=[("fpv","FPV"),("Compact","Compact Portable")])
    fav = StringField("Favorite drone you have: ")
    submit = SubmitField("Submit")

################


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/mydrones')
def mydrones():
    return render_template("mydrones.html")

@app.route('/yourdrones',methods =("GET","POST"))
def yourdrones():

    form = drone()

    if form.validate_on_submit():
        session['amount']=form.amount.data
        session['type'] = form.whatType.data
        session['better'] = form.better.data
        session['fav'] = form.fav.data
        
        return redirect(url_for('results'))
    return render_template("urdrone.html",form=form)

@app.route('/results')
def results():
    return render_template("cooldrone.html")

if __name__ == '__main__':
    app.run(debug=True)