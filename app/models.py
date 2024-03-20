from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    permissions = db.Column(db.String(256))  # NOTE: this will be stored like this `1,2,3,4,5, `

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'permissions': self.permissions.split(',')
        }


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
        else:
            raise Exception('Role Not Found')

    def get_role(self) -> Role | None:
        role = Role.query.filter_by(id=self.role_id).first()

        if role:
            return role
        else:
            return None

    def is_admin(self):
        role = Role.query.filter_by(name='Admin').first()

        return self.role_id == role.id

    def to_json(self):
        role = self.get_role()

        if role:
            role = role.to_json()
        else:
            role = None

        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': role
        }

    def __str__(self):
        return str(self.id) + ': ' + self.email


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salary = db.Column(db.Float)

    def to_json(self):
        return {
            'id': self.id,
            'salary': self.salary
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    price = db.Column(db.Float)
    img = db.Column(db.String(256))
