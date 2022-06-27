from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///../store.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/catalog")
def catalog():
    from app.models.Item import Item
    return render_template("catalog.html", items=Item.query.all())

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)