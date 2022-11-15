from functools import wraps
from app.server import redirect, url_for, current_user, flash


def block_authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            flash("Forbidden: Please logout", category="info")
            return redirect(url_for("index"))
        else:
            return f(*args, **kwargs)
    return decorated_function

def block_unauthenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not(current_user.is_authenticated):
            flash("Forbidden: User is not logged in", category="info")
            return redirect(url_for("index"))
        else:
            return f(*args, **kwargs)
    return decorated_function

