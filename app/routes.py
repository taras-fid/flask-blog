from flask import request, session, make_response, abort, render_template
from app import app, db, mail
from app.models import User
from flask_mail import Message

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()

        if not data:
            return 'Bad Request', 400

        email = data.get('email')
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return 'error: email already in use', 422

        user = User(username='test', email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        msg = Message(
            subject='Registration letter',
            sender='noreply@employer.com',
            recipients=[email]
        )
        msg.html = render_template('template_letter.html', content=render_template('register_letter.html'))
        mail.send(msg)

        return make_response(user.to_json())


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        if not data:
            return 'Bad Request', 400

        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()

        if user and user.is_password_correct(password):
            session['user_id'] = user.id
            return make_response(user.to_json())

        return 'error: no user found', 422


@app.route('/add-role/<user_id>', methods=['POST'])
def add_role_for_user(user_id):
    try:
        if request.method == 'POST':
            if session.get('user_id'):
                current_user = User.query.filter_by(id=session.get('user_id')).first()

                if current_user.is_admin():
                    data = request.get_json()

                    if not data:
                        return 'Bad Request', 400

                    role_id = data.get('role_id')

                    user = User.query.filter_by(id=user_id).first()
                    user.set_role(role_id)
                    db.session.commit()

                    return make_response(user.to_json(), 200)
                else:
                    abort(404)

            else:
                return 'User is not authenticated', 401

    except Exception as ex:
        if str(ex) == 'Role Not Found':
            return str(ex), 404
        elif str(ex) == '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.':
            return str(ex), 404
        else:
            return str(ex), 500


@app.route('/add-permission/<role_id>', methods=['POST'])
def add_permission_for_role(role_id):
    try:
        if request.method == 'POST':
            if session.get('user_id'):
                current_user = User.query.filter_by(id=session.get('user_id')).first()

                if current_user.is_admin():
                    data = request.get_json()

                    if not data:
                        return 'Bad Request', 400

                    role_id = data.get('permission_id')

                    # todo: add BL(business-logic) to create new Permission
                    # todo: return new Permission that was created
                else:
                    abort(404)

            else:
                return 'User is not authenticated', 401

    except Exception as ex:
        if True:
            pass
            # todo: add error/exception validation
        elif str(ex) == '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.':
            return str(ex), 404
        else:
            return str(ex), 500