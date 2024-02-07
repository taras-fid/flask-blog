from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import User


@app.route('/')
def index():
    return str(session.get('user', 'U must login!'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            return 'error: email already in use', 422

        user = User(username='test', email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return str(user)
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.is_password_correct(password):
            session['user'] = user.to_json()
            return redirect(url_for('index'))

        return 'error: no user found', 422

    return render_template('login.html')
