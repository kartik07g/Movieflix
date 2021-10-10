from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "movieflix"

# Database
cluster = MongoClient("mongodb+srv://dpradnya:India@11@cluster0.xzrf3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Movieflix"]
# colle1 = db['login']

# Routes
from user import routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")

app.run(debug=True)