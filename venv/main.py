from flask import Flask, render_template
from pymongo import MongoClient
import urllib.parse
from flask import request
import uuid


username = urllib.parse.quote_plus('kartik07g')
password = urllib.parse.quote_plus('k@123')

app = Flask(__name__)

app.secret_key = "movieflix"
client = MongoClient("mongodb+srv://%s:%s @cluster0.sht6k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" % (
    username, password))
db = client['Movieflix']
collection = db['users']
collection.insert_one({"_id": "656464", "name":"kartik"})
# print(insert)
# print(db)


# client = MongoClient('localhost',27017)
# db = client.users()

#
# class User:
#
#     def start_session(Self, user):
#         del user['password']
#         session['logged_in'] = True
#         session['user'] = user
#         return jsonify(user), 200
#
#     def signup(self):
#
#         # Create the user object
#         user = {
#             "_id": uuid.uuid4().hex,
#             "name": request.form.get('name'),
#             "email": request.form.get('email'),
#             "password": request.form.get('password')
#         }
#
#         # Encrypt the password
#         # user['password'] = pbkdf2_sha256.encrypt(user['password'])
#
#         # Check for existing email address
#
#         if db.user.find_one({"email": user['email']}):
#             return jsonify({"error": "EMail already in use"}), 400
#
#         # users is a collection in db where we want to save user details
#         if db.users.insert_one(user):
#             return self.start_session(user)
#
#         return jsonify({"error": "SignUp Failed"}), 400
#
#     def signout(self):
#         session.clear()
#         return redirect('/')


@app.route("/", methods=['GET', 'POST'])
def rej():

    if (request.method == 'POST'):
        if (request.form.get('reg')):
            name = request.form.get('fname')
            email = request.form.get('email2')
            phone = request.form.get('phone')
            password = request.form.get('passd')
            cpass = request.form.get('cpass')
            print("71", cpass)

            user = {
                "_id": uuid.uuid4().hex,
                "name": name,
                "email": email,
                "phone" : phone,
                "password": password
            }
            print(user)

            if (password == cpass):
                if db.user.find_one({"email": user['email']}):
                    return jsonify({"error": "EMail already in use"}), 400
                try:
                    if db.users.insert_one(user):
                        print('user added')
                        return render_template("rejister.html")
                except e :
                    print('***',e)
                

#we have return modal of password confirmation
        if (request.form.get('login')):
            email = request.form.get('email')
            password = request.form.get('password')
            print(email + password)
            return render_template("index.html")

    return render_template("rejister.html")


def rej():
    return render_template("rejister.html")


@app.route("/index")
def index():
    return render_template("index.html")


app.run(debug=True)
