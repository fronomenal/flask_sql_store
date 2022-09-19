from app.server import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    usrname = db.Column(db.String(length=30), nullable=False, unique=True)
    usrbudget = db.Column(db.Integer(), nullable=False, default=999)
    usrmail = db.Column(db.String(length=60), nullable=False, unique=True)
    _usrpass = db.Column(db.String(length=60), nullable=False)
    items = db.relationship("Item", backref="owned_by", lazy=True)

    @property
    def usrpass(self):
        return self._usrpass

    @usrpass.setter
    def usrpass(self, inpass):
        self._usrpass = bcrypt.generate_password_hash(inpass).decode("utf-8")