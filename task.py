from flask import Flask

import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    price = db.Column(db.Float)
    img = db.Column(db.String(256))


@app.route('/')
def main():
    pass
    # TODO: 1) return paginated  products
    # TODO: 2) add filter to return products by name
    # TODO: 3) add filter to return products by price
    #  (think about the way you can check is price more or less than filter value)

    # TODO: 1) повернути пагіновані товари
    # TODO: 2) додати фільтр для повернення товарів за назвою
    # TODO: 3) додати фільтр для повернення товарів за ціною
    # (Подумайте, як можна перевірити, чи ціна більша або менша за значення фільтра)