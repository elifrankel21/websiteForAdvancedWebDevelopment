from flask import Flask, render_template, request, redirect, send_file, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
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
import Image
import json
keys = db.keys()
print(keys)
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)
class LoginForm(FlaskForm):
    name = StringField(label="Username:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Submit", validators=[DataRequired()])


class RequestLogin(FlaskForm):
    name = StringField(label="Name:", validators=[DataRequired()])
    student_id = StringField(label="Student ID:", validators=[DataRequired()])
    home_email = StringField(label="Home Email (to contact you):",
                             validators=[DataRequired()])
    resume = StringField(label="Why do you want to join?",
                         validators=[DataRequired()])
    username = StringField(label="What username do you want?",
                           validators=[DataRequired()])
    password = StringField(label="What password do you want?",
                           validators=[DataRequired()])
    tos = StringField(label="Y/N Follow all TOS",
                           validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/request", methods=["GET", "POST"])
def request():
    form = RequestLogin()
    if form.validate_on_submit():
        name = form.name.data
        student_id = form.student_id.data
        home_email = form.home_email.data
        resume = form.resume.data
        username = form.username.data
        password_user = form.password.data
        tos = form.tos.data
        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "noreplypython0@gmail.com"
        receiver_email = [
            "elifrankel4@gmail.com", "maracuchoamericano@gmail.com"
        ]
        password = "dielepwyvzykhvti"
        message = f"New user wants access to schoolhub. Here's their info \n name = {name} \n  Student Id = {student_id} \n Home Email = {home_email} \n Why want to join = {resume}\n What username they want {username}\n Password they want {password_user}."
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, password)
            for person in receiver_email:
                server.sendmail(sender_email, person, message)
            return redirect("/")

    return render_template("request.html", form=form)


@app.route("/uploadfile")
def upload():
    return render_template("upload.html")


@app.route("/bannedusers")
def banned():
    return render_template("bannedusers.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password_form = form.password.data
        name_check = str(db.get(name))
        password_form = str(password_form)
        if name_check == password_form:
            global onetimepass
            onetimepass = random.randint(1, 69420420)
            return redirect(f"/games/{onetimepass}")
        else:
            return redirect("/error")

    return render_template("login.html", form=form)


@app.route("/cookieclickerurl/<password>")
def cookie_clicker(password):
    if password == str(onetimepass):
        return render_template("cookieclicker.html")
    else:
        return redirect("/")


@app.route("/2048/<password>")
def zoqb(password):
    if password == str(onetimepass):
        return render_template("2048.html")
    else:
        return redirect("/")


# apply to join
@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/games/<password>")
def games(password):
    if password == str(onetimepass):
        return render_template(
            "games.html",
            cookieclickerurl=f"/cookieclickerurl/{password}",
            slope=f"/slope/{onetimepass}",
            tictactoe=f"/tictactoe/{tictactoe}",
            two_thousand_forty_eight=f"/2048/{onetimepass}")
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
    game_requested = StringField(
        label="What game would you like added onto the website?",
        validators=[DataRequired()])
    submit = SubmitField(label="Submit Feedback")


# @app.route("/make-custom-url-img", method=["GET"])
# def make_url():
# file = request.files.get['image']
# img = Image.open(file.stream)
# return None




@app.route("/requestgame", methods=["GET", "POST"])
def gamerequest():
    form = GameRequest()
    if form.validate_on_submit():
        game_requested = form.game_requested.data
        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "noreplypython0@gmail.com"
        receiver_email = [
            "elifrankel4@gmail.com", "maracuchoamericano@gmail.com"
        ]
        password = "dielepwyvzykhvti"
        message = f"A person has requested for {game_requested}"
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, password)
            for person in receiver_email:
                server.sendmail(sender_email, person, message)
            return redirect(f"/games/{onetimepass}")
    return render_template("gamerequest.html", form=form)
class BanForm(FlaskForm):
    username = StringField(
        label="Username: ",
        validators=[DataRequired()])
    reason = StringField(
        label="Reason: ",
        validators=[DataRequired()])
    adminu = StringField(
        label="Admin Username: ",
        validators=[DataRequired()])    
    adminp = StringField(
        label="Admin Password: ",
        validators=[DataRequired()])
    submit = SubmitField(label="Submit Feedback")
@app.route("/ban", methods=["GET", "POST"])
def ban():
  form = BanForm()
  if form.validate_on_submit():
    if (form.adminu.data == "eli" and form.adminp.data == "3704"):
      del db[f"{form.username.data}"]
      ###
      user = form.username.data
      reason = form.reason.data
      
      port = 587
      smtp_server = "smtp.gmail.com"
      sender_email = "noreplypython0@gmail.com"
      receiver_email = [
            "elifrankel4@gmail.com"
        ] # "maracuchoamericano@gmail.com"
      password = "dielepwyvzykhvti"
      message = f"{form.username.data} Banned:\nReason: {form.reason.data}\n"
      with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, password)
            for person in receiver_email:
                server.sendmail(sender_email, person, message)
  return render_template("banhammer.html", form=form)

class AddUser(FlaskForm):
    username = StringField(
        label="Username: ",
        validators=[DataRequired()])
    password = StringField(
        label="Password: ",
        validators=[DataRequired()])
    adminu = StringField(
        label="Admin Username: ",
        validators=[DataRequired()])    
    adminp = StringField(
        label="Admin Password: ",
        validators=[DataRequired()])
    submit = SubmitField(label="Submit Feedback")
@app.route("/adduser", methods=["GET", "POST"])
def UserAdd():
  form = AddUser()
  if form.validate_on_submit():
    if (form.adminu.data == "eli" and form.adminp.data == "3704"):
      db[f"{form.username.data}"] = f"{form.password.data}"
      print(f"{form.username.data} has been added by and admin!")
  return render_template("adduser.html", form=form)
@app.route("/tos")
def Tos():
  return render_template("tos.html")
app.run(debug=True, host='0.0.0.0')