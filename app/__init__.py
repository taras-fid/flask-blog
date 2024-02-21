from flask import Flask

import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
app.permanent_session_lifetime = timedelta(minutes=90)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app import routes
from app import models
