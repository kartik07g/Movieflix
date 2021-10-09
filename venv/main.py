from flask import Flask, render_template
app = Flask(__name__)

# Routes
from user import routes

@app.route("/")
def index():
    return render_template("index.html")
app.run(debug=True)