from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
SECRET_KEY = os.urandom(32)




app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)
class Login(FlaskForm):
  username = StringField("Username", [DataRequired()])
  password = StringField("Password", [DataRequired()])
  submit = SubmitField("Login")


@app.route("/signup", methods=["GET","POST"])
def signup():
  form = Login()
  if form.validate_on_submit():
    if form.username.data == "eli" and form.password.data == "3704":
       return redirect("/")
    else:
       return "<h1>Wrong password</h1>"
  return render_template("index.html", form=form)


@app.route("/games")
def games():
  return render_template("games.html")
@app.route("/")
def welcome():
  return render_template("welcome_page.html")
app.run(debug=True, host='0.0.0.0')



