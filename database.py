# database.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:221022@localhost/beelaboo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
sqldb = SQLAlchemy()


# create app
def create_app():
    sqlDB = SQLAlchemy(app)
    sqlDB.init_app(app)
    sqlDB.create_all()
    return app