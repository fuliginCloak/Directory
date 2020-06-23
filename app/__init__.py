
from flask import Flask
from flask_admin import  Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config




app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = 'flaskdrive '
login = LoginManager(app)
login.login_view= 'login'
admin = Admin(app,'BOHN Management')

app.config.from_object(Config)
db = SQLAlchemy(app)
# db.init_app(app)
# with app.app_context():
#     db.create_all()
migrate = Migrate(app,db)

from app import routes, models





