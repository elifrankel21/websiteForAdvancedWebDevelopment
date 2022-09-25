from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import smtplib
import time
import requests
SECRET_KEY = os.urandom(32)
#stack overflow fucked me over
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)

class AppointmentForm(FlaskForm):
  name = StringField(label="Name:", validators=[DataRequired()])
  email = StringField(label="School Email", validators=[DataRequired()])
  resume = StringField(label="Why do you want access to this website?", validators=[DataRequired()]) 
  username = StringField(label="What do you want your username to be?", validators=[DataRequired()]) 
  password = StringField(label="What do you want yout password to be?", validators=[DataRequired()]) 
  submit = SubmitField(label="Submit")





class Login(FlaskForm):
  username = StringField("Username", [DataRequired()])
  password = StringField("Password", [DataRequired()])
  submit = SubmitField("Login")
@app.route("/signup", methods=["GET","POST"])
def signup():
  form = Login()
  if form.validate_on_submit():
    if form.username.data == "eli" and form.password.data == "3704":
     level = 3
     return redirect("/games")
  if form.validate_on_submit():
    if form.username.data == "annak" and form.password.data == "8625":
     return redirect("/games")
    else:
       return redirect("https://i.ytimg.com/vi/L7yDR_8sHFs/maxresdefault.jpg") #send you to a meme about worng password
  
  
  
  return render_template("index.html", form=form)
@app.route("/games")
def games():
  return render_template("games.html")



@app.route("/")
def welcome():
  return render_template("welcome_page.html")




@app.route("/book_an_appointment", methods=["GET","POST"])
def booking_an_appointment():
    appointment_form = AppointmentForm()
    if appointment_form.validate_on_submit():
      c_name = appointment_form.name.data
      c_email = appointment_form.email.data
      c_username = appointment_form.username.data
      
      port = 587  # For starttls
      smtp_server = "smtp.gmail.com"
      sender_email = "noreplypython0@gmail.com"
      receiver_email = ["elifrankel4@gmail.com"] #maracuchoamericano@gmail.com
      password = "dielepwyvzykhvti"
      message = f"A person has requested to gain access to the website. Name. {appointment_form.name.data}\n School Email. {appointment_form.email.data}\n  Why they want to join. {appointment_form.resume.data}\n Username: {appointment_form.username.data}\nPassword: {appointment_form.password.data}"

      with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo() 
        server.login(sender_email, password)
        for person in receiver_email:
          server.sendmail(sender_email, person, msg=message)


      return redirect("/")
    return render_template("book.html", form=appointment_form)





app.run(debug=True, host='0.0.0.0')



