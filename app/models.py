from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password_hash = db.Column(db.String(120), index = True, unique = False)


    def __repr__(self):
        return  f'<User {self.username}>'

    def __tablename__(self):
        return 'User'


User.__repr__