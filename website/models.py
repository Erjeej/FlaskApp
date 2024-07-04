from . import db #importing from within the website package (folder) - db is defined object in __init__.py. Ff it was from outside this directory it would be - from website import db 
from flask_login import UserMixin

class User (db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)