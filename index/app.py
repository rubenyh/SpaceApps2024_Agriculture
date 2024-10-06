from flask import Flask, render_template, request
from weather_api import gather_data_name
from forecast import windChill

def get_color_from_score(score):
    red = int(255 * (1 - score))
    green = int(255 * score)
    return f"rgb({red}, {green}, 0)"


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
    wind_speed = float(request.args.get("wind_speed"))
    weather = request.args.get("weather")
    state = request.args.get("state")
    temp = float(request.args.get("temp")) - 275.15  # Convert from Kelvin to Celsius
    windchill = windChill(wind_speed, temp + 275.15)
    temp = float("{:.2f}".format(temp))
    humidity = float(request.args.get("humidity"))
    pressure = request.args.get("pressure")
    visibility = float(request.args.get("visibility"))
    
    # Calculate the suitability score based on the data
    # 1. Temperature Score
    if 10 <= temp <= 30:
        temp_score = 1
    elif (5 <= temp < 10) or (30 < temp <= 35):
        temp_score = 0.5
    else:
        temp_score = 0

    # 2. Humidity Score
    if 40 <= humidity <= 70:
        humidity_score = 1
    elif (20 <= humidity < 40) or (70 < humidity <= 80):
        humidity_score = 0.5
    else:
        humidity_score = 0

    # 3. Weather Description Score (simplified for clear sky)
    if "clear" in weather.lower():
        weather_score = 1
    else:
        weather_score = 0.5  # You can adjust this depending on how other weather conditions are handled

    # 4. Wind Speed Score
    if 0.5 <= wind_speed <= 5:
        wind_score = 1
    elif 5 < wind_speed <= 10:
        wind_score = 0.5
    else:
        wind_score = 0

    # 5. Visibility Score
    if visibility >= 10000:
        visibility_score = 1
    elif visibility >= 5000:
        visibility_score = 0.5
    else:
        visibility_score = 0

    # Calculate the final Farming Suitability Score
    farmingScore = (
        0.3 * temp_score +
        0.2 * humidity_score +
        0.2 * weather_score +
        0.1 * wind_score +
        0.1 * visibility_score
    )

    # Pass the retrieved data and the farming suitability score to the template
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
        visibility=visibility,
        windchill=windchill,
        farmingScore=float("{:.2f}".format(farmingScore)),
        color=get_color_from_score(farmingScore)
    )
