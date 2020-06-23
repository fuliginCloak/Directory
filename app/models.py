from app import db
from datetime import  datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login



@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password_hash = db.Column(db.String(120), index = True, unique = False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return  f'<User {self.username}>'

 

User.__repr__


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    db_title = db.Column(db.String(64), index = True)
    db_state = db.Column(db.String(2))
    db_county = db.Column(db.String(64))
    db_price = db.Column(db.Integer, index = True)
    db_acres = db.Column(db.Float, index = True)
    db_short = db.Column(db.String(64))
    db_long = db.Column(db.String(500), index = True)
    db_images = db.Column(db.String)

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Listing:{self.db_title} - {self.db_state} - {self.db_county} - {self.db_price} - {self.db_acres} - {self.db_short}  - {self.db_short}  - {self.timestamp}  >'


Listing.__repr__

