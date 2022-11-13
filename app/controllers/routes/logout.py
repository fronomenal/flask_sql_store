from app.server import server, redirect, url_for, logout_user, User, flash
from app.utils.forms import LoginForm

@server.route("/logout", methods=["GET", "POST"])
def logout():
  logout_user()

  flash("Logged out successfully", category="info")
  
  return redirect(url_for("index"))