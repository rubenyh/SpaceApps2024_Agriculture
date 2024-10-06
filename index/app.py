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
    # Retrieve the city weather data from the form
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    temp = float(request.args.get("temp")) - 275.15
    temp = "{:.2f}".format(temp)
    humidity = request.args.get("humidity")
    weather = request.args.get("weather")
    wind_speed = request.args.get("wind_speed")
    pressure = request.args.get("pressure")
    visibility = request.args.get("visibility")
    
    # Pass the retrieved data to the template
    return render_template(
        "results.html", 
        name=name, 
        country=country, 
        state=state, 
        temp=temp, 
        humidity=humidity, 
        weather=weather,
        wind_speed=wind_speed,
        pressure=pressure,
        visibility=visibility
    )