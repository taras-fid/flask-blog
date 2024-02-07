from sqlalchemy import ForeignKey
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def is_password_correct(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_role(self, role_id):
        if Role.query.filter_by(id=role_id).first():
            self.role_id = role_id
        raise Exception('No such role')

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role_id': self.role_id
        }

    def __str__(self):
        return str(self.id) + ': ' + self.email


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    permissions = db.Column(db.String(256))  # NOTE: this will be stored like this `1,2,3,4,5, `


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)


class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    salary = db.Column(db.Float)
