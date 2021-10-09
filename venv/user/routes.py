from flask import Flask
from main import app
from user.models import User

@app.route('/user/signup', methods=['POST'])

def signup():
    return User().signup()