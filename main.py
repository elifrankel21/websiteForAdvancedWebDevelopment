from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
  return render_template("welcome_page.html")

app.run(debug=True, host='0.0.0.0')



