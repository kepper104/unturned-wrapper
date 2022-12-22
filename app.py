import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def def_app():
    # url = "http://movie-quotes-2.herokuapp.com/api/v1/quotes/random"
    # response = requests.get(url).json()

    return "Hello there"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')