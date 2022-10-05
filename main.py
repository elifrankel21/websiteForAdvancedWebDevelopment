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


# I a backing everything up and going to work on a js login system for now so that if saves to cookies and they cannot even see the website without it so that if a teacher trys to get on they cannot even see it.

app = Flask(__name__)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)




@app.route("/login", methods=["GET","POST"])
def login():
  return render_template("login.html",)



@app.route("/games")
def games():
  return render_template("games.html")



@app.route("/")
def welcome():
  return render_template("welcome_page.html")
@app.route("/testing")
def testing():
  return render_template("testing.html")



# @app.route("/request", methods=["GET","POST"])
# def booking_an_appointment():
#     appointment_form = AppointmentForm()
#     if appointment_form.validate_on_submit():
#       c_name = appointment_form.name.data
#       c_email = appointment_form.email.data
#       c_username = appointment_form.username.data
      
#       port = 587  # For starttls
#       smtp_server = "smtp.gmail.com"
#       sender_email = "noreplypython0@gmail.com"
#       receiver_email = ["elifrankel4@gmail.com"] #maracuchoamericano@gmail.com
#       password = "dielepwyvzykhvti"
#       message = f"A person has requested to gain access to the website. Name. {appointment_form.name.data}\n School Email. {appointment_form.email.data}\n  Why they want to join. {appointment_form.resume.data}\n Username: {appointment_form.username.data}\nPassword: {appointment_form.password.data}"

#       with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo()
#         server.starttls()
#         server.ehlo() 
#         server.login(sender_email, password)
#         for person in receiver_email:
#           server.sendmail(sender_email, person, msg=message)


#       return redirect("/")
#     return render_template("book.html", form=appointment_form)




@app.route("/slope")
def slope():
  return render_template("slope.html")
@app.route("/chat")
def chat():
  return render_template("chat.html")




@app.route("/tictactoe")
def tictactoe():
  return render_template ('tictactoe.html')


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
    
    
  
  


app.run(debug=True, host='0.0.0.0')



