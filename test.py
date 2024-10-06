import requests
url = "http://api.openweathermap.org/geo/1.0/direct"
api_key = "b05ad82a832f5da790b48645e5943fc7"

params = {
    "appid": api_key,   # Include your API key
    "q": "ensenada",
    "limit": 100
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()  # Parse JSON response
    #print("Data:", data["weather"])  # Print the retrieved weather data
    for i in data:
        print(i["name"], i["country"], i["lat"], i["lon"])
    j = int(input("n: ")) -1
    print(data[j]["name"], data[j]["country"], data[j]["state"])
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")