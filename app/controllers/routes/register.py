import random
from app.server import server, redirect, url_for, render_template, db,  User, flash, login_user
from app.utils.forms import RegisterForm
from app.controllers.actions.cus_auth_check import block_authenticated

money = [900, 1200, 1500]

@server.route("/sign-up", methods=["GET", "POST"])
@block_authenticated
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        newusr = User(usrname=form.username.data, usrpass=form.password1.data, usrmail=form.email.data, usrbudget=random.choice(money))
        db.session.add(newusr)
        db.session.commit()

        login_user(newusr)
        flash(f"Account created successfully for: {newusr.usrname}", category="success")

        return redirect(url_for("catalog"))

    if form.errors != {}:
        for e in form.errors.values():
            flash(f"There was a problem with user input: {e}", category="danger")

    return render_template("register.html", form=form)