from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Home Page"


@app.route("/index")
def index():
    return "<h1>Welcome to the Index Page<h1>"


if __name__ == "__main__":
    app.run(debug=True)
