from flask import Flask

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    pass


@app.route("/add")
def add():
    pass


if __name__ == "__main__":
    app.run(debug=True)
