from flask import Flask, render_template, request
from weather_api import gather_data_name

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    city = request.args.get("q")
    data = gather_data_name(city)
    return render_template("search.html", cities=data)


@app.route("/results")
def results():
    data = request.args.get("data")
    print(data)
    return render_template("results.html", data=data)