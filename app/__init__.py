from flask import Flask
from flask_admin import  Admin
from config import Config

app = Flask(__name__)
admin = Admin(app,'BOHN Management')

app.config.from_object(Config)

from app import routes
