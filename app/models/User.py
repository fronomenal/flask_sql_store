from app.server import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    usrname = db.Column(db.String(length=30), nullable=False, unique=True)
    usrbudget = db.Column(db.Integer(), nullable=False, default=999)
    usrmail = db.Column(db.String(length=60), nullable=False, unique=True)
    usrpass = db.Column(db.String(length=60), nullable=False)
    items = db.relationship("Item", backref="owned_by", lazy=True)
