from app.server import server, redirect, url_for, render_template, db,  User, flash
from app.utils.forms import RegisterForm

@server.route("/sign-up", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        newusr = User(usrname=form.username.data, usrpass=form.password1.data, usrmail=form.email.data)
        db.session.add(newusr)
        db.session.commit()

        return redirect(url_for("catalog"))

    if form.errors != {}:
        for e in form.errors.values():
            flash(f"There was a problem with user input: {e}", category="danger")

    return render_template("register.html", form=form)