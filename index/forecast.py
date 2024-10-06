import requests

def windChill(V, T):
    V = V * 2.23694
    T = 1.8*(T-273) + 32.
    R =35.74 + 0.6215 * T  - 35.75 * (V**0.16) +0.4275 * T * (V**0.16)
    print("wind chill in farenheit: ", int(R))

def forecast(lat,lon):
    url = "https://api.openweathermap.org/data/2.5/forecast?"
    api_key = "b05ad82a832f5da790b48645e5943fc7"
    params = {
    #"year": "?",
    "lat": lat,
    "lon": lon,
    "appid": api_key,   # Include your API key
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse JSON response
        #print("Data:", data["weather"])  # Print the retrieved weather data
        j = 0
        for key, value in data.items():
            print(key)
            if key == "list":
                for i in value:
                    j = j + 3
                    print(j, "hour forecast")
                return value

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


s = forecast(39,41)