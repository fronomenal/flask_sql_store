from app.server import db, bcrypt, login_manager, UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
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

    def verify_pass(self, password):
        return bcrypt.check_password_hash(self._usrpass, password)