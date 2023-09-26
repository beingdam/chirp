from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f995a75ad60845f7b3fac2ae8c9504be'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

from chirp import routes