from app.server import server, redirect, url_for, logout_user, User, flash
from app.utils.forms import LoginForm
from app.controllers.actions.cus_auth_check import block_unauthenticated

@server.route("/logout", methods=["GET", "POST"])
@block_unauthenticated
def logout():
  logout_user()

  flash("Logged out successfully", category="info")
  
  return redirect(url_for("index"))