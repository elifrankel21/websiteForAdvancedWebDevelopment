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
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import pandas
# I a backing everything up and going to work on a js login system for now so that if saves to cookies and they cannot even see the website without it so that if a teacher trys to get on they cannot even see it.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"

db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)



SECRET_KEY = os.urandom(32)
#stack overflow fucked me over

app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True,nullable=False)
  email = db.Column(db.String(100), unique=True,nullable=False)
  password = db.Column(db.String(20), unique=False,nullable=False)







# new_user = User(username="eli", email="fakeemail@gmail.com", password="3704")

# db.session.add(new_user)
# db.session.commit()
  

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id)) 

class Register(FlaskForm):
  name = StringField(label="Name:", validators=[DataRequired()])
  email = StringField(label="School Email", validators=[DataRequired()])
  password = StringField(label="Password:", validators=[DataRequired()])
  submit = SubmitField(label="Submit")
  



@app.route("/request", methods=["GET","POST"])
def register():
  form = Register()
  if request.method == "POST":
    if form.validate_on_submit():
      email = request.form.get('email')
      password = request.form.get('password')
      name = request.form.get('name')
      file = open("users.txt", "a")
      file.write(f"{email},{name},{password}")
      return redirect("/games")
      
      
  
  return render_template("register.html",form=form)
 

  
# @app.route("/request", methods=["GET","POST"])
# def register():
#     form = Register()
#     if request.method == "POST":
#       #this generates hashed password and salting to make it less easy to attempt to hack into the website and steal an account (thought it would be cool to add)
#         hash_and_salted_password = generate_password_hash(
#             request.form.get('password'),
#             method='pbkdf2:sha256',
#             salt_length=8
#         )
#       #this uses the User() class to add it to the database (so they can log in, in the future)
#         new_user = User(
#             email=request.form.get('email'),
#             username=request.form.get('name'),
#             password=hash_and_salted_password,
#         )

#         db.session.add(new_user)
#         db.session.commit()

#       #This tells the website that the user has already logged in and is now authenticated to go to /games
#         login_user(new_user)

      
#         return redirect("/games")
#     return render_template("register.html", form=form)
  


  








#form that users are required to use to log in
class Login(FlaskForm):
  username = StringField("Email", [DataRequired()])
  password = StringField("Password", [DataRequired()])
  submit = SubmitField("Login")

  
@app.route("/login", methods=["GET","POST"])
def login():
  form = Login()
  if form.validate_on_submit():
    if request.method == "POST":
      email = request.form.get("email")
      password = request.form.get("password")
      df = pandas.read_csv("users.txt")
      email_check = df["email"].loc[email]
      if email_check == None:
        return "<h1>That email does not exist</h1>"
      else:
        password_csv = df[email_check]["password"]
        if password == password_csv:
          return redirect("/games")
          
  return render_template("index.html", form=form)



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
app.run(debug=True, host='0.0.0.0')



