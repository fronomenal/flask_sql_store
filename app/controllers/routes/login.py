from app.server import server, redirect, url_for, render_template, db, login_user, User, flash
from app.utils.forms import LoginForm

@server.route("/login", methods=["GET", "POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    get_user = User.query.filter_by(usrname=form.username.data).first();
    if (get_user and get_user.verify_pass(form.password.data)):
        login_user(get_user)
        flash(f"You are now logged in as: {get_user.usrname}", category="success")
        return redirect(url_for("catalog"))

    flash("Failed to log in. Please try again with different credentials", category="danger")

  return render_template("login.html", form=form)