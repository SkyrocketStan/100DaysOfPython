import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)
CURRENT_YEAR = datetime.datetime.now().year


@app.route('/')
def index():
    # current_year = datetime.datetime.now().year
    return render_template("index.html", year=CURRENT_YEAR)


@app.route('/guess/<name>')
def name_guess(name: str):
    payload = {'name': name}
    response_gender = requests.get("https://api.genderize.io/", params=payload)
    response_gender.raise_for_status()
    gender = response_gender.json().get("gender", "Unknown")
    response_age = requests.get("https://api.agify.io/", params=payload)
    response_age.raise_for_status()
    age = response_age.json().get("age", "Unknown")
    return render_template('guess.html',
                           name=name.capitalize(), gender=gender, age=age,
                           year=CURRENT_YEAR)


if __name__ == '__main__':
    app.run(debug=True)
