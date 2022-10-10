from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import time
import requests
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pandas
from replit import db
import smtplib
import random

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
  name = StringField(label="Username:", validators=[DataRequired()])
  password = StringField(label="Password:", validators=[DataRequired()])
  submit = SubmitField(label="Submit", validators=[DataRequired()])


@app.route("/login", methods=["GET","POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      name = form.name.data
      password_form = form.password.data
      name_check = str(db.get(name))
      password_form = str(password_form)
      if name_check == password_form:
        global onetimepass
        onetimepass = random.randint(1,6924200000)
        return redirect(f"/games/{onetimepass}")
      else:
        return redirect("/error") 
      
    
  
  return render_template("login.html",form=form)



@app.route("/cookieclickerurl/<password>")
def cookie_clicker(password):
  if password == str(onetimepass):
    return render_template("cookieclicker.html")
  else:
    return redirect("/")
    

@app.route("/minecraft")
def minecraft():
    return render_template("minecraft.html")

@app.route("/error")
def error():
  return render_template("error.html")
    
  



@app.route("/games/<password>")
def games(password):  
  if password == str(onetimepass):
    return render_template("games.html",cookieclickerurl=f"/cookieclickerurl/{password}",slope=f"/slope/{onetimepass}",tictactoe=f"/tictactoe/{tictactoe}")
  else:
    return redirect("/")


@app.route("/")
def welcome():
  return render_template("welcome_page.html")
@app.route("/quick")
def testing():
  return render_template("quickdraw.html")



@app.route("/slope/<password>")
def slope(password):
  if password == str(onetimepass):
    return render_template("slope.html")
  else:
    return redirect("/")

@app.route("/chat")
def chat():
  return render_template("chat.html")




@app.route("/tictactoe/<password>")
def tictactoe(password):
  if password == str(onetimepass):
    return render_template("tictactoe.html")

@app.route("/onetrickmage")
def onetrickmage():
  return render_template("onetrickmage.html")

class GameRequest(FlaskForm):
  game_requested = StringField(label="What game would you like added onto the website?",validators=[DataRequired()])
  submit = SubmitField(label="Submit Feedback")
  


@app.route("/requestgame",methods=["GET","POST"])
def gamerequest():
  form = GameRequest()
  if form.validate_on_submit():
    game_requested = form.game_requested.data
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "noreplypython0@gmail.com"
    receiver_email = ["elifrankel4@gmail.com","maracuchoamericano@gmail.com"] 
    password = "dielepwyvzykhvti"
    message = f"A person has requested for {game_requested}"
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo() 
        server.login(sender_email, password)
        for person in receiver_email:
          server.sendmail(sender_email, person, message)
        return redirect("/games")
  return render_template("gamerequest.html",form=form)
  
  


app.run(debug=True,host='0.0.0.0')




