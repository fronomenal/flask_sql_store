from app.server import server, redirect, url_for, render_template, db,  User, flash
from app.utils.forms import LoginForm

@server.route("/login", methods=["GET", "POST"])
def login():
  form = LoginForm()
  return render_template("login.html", form=form)