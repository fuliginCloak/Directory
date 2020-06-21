
from flask import Flask
from flask_admin import  Admin
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
admin = Admin(app,'BOHN Management')

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, models


