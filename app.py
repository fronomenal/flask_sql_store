from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Flask says hello<h1>"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)