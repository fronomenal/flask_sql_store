from app.server import server, render_template, Item

@server.route("/catalog")
def catalog():
    return render_template("catalog.html", items=Item.query.all())