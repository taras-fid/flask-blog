from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User


@app.route('/')
def index():
    return 'Main'


@app.route('/register', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            return 'error: email already in use', 422

        user = User(username='test', email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return 'ok'
    return render_template('login.html')