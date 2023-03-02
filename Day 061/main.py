from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from login_form import LoginForm

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if not login_form.validate_on_submit():
        return render_template("login.html", form=login_form)

    if login_form.email.data == 'email@email.com' and login_form.password.data == "123456789":
        return render_template("success.html")

    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
