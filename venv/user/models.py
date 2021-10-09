from flask import Flask, jsonify, request, session, redirect
from main import db
import uuid
from passlib.hash import pbkdf2_sha256

class User:
    

    def start_session(Self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
    
    def signup(self):
        
        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address

        if db.user.find_one({"email":user['email']}):
            return jsonify({ "error": "EMail already in use"}), 400


        # users is a collection in db where we want to save user details
        if db.users.insert_one(user):
            return self.start_session(user)
    

        return jsonify({"error": "SignUp Failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')