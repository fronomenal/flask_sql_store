from app.server import server, render_template

@server.route("/")
@server.route("/home")
def index():
    return render_template("index.html")