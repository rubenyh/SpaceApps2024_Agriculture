from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Function to retrieve weather data from OpenWeather API
def get_weather_data(city_name):
    api_key = 'b05ad82a832f5da790b48645e5943fc7'  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    city = request.args.get('q')  # Get the search query from the URL
    if city:
        data = get_weather_data(city)
        if data:
            return render_template('secondarypage.html', data=data, city=city)
        else:
            return render_template('secondarypage.html', error="City not found", city=city)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
