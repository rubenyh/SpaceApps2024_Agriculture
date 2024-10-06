import requests

s = input("place:")
#Recursion Bitch
def listprint(data):
    for i in data:
        if isinstance(i, dict):
            dictprint(i)
        elif isinstance(i, list):
            listprint(i)
        else:
            print(i)
    return

def dictprint(data):
    for key, value in data.items():
        if isinstance(value, list) or isinstance(value, dict):
            print(key)
            if isinstance(value, dict):
                dictprint(value)
            else:
                listprint(value)
        else:
            print(f"{key}: {value}")  # Print the individual value
# Define the API endpoint and your API key
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "b05ad82a832f5da790b48645e5943fc7"

#s = input("Insert city name: ")
params = {
    "appid": api_key,   # Include your API key
    "q": s
}

# Make the GET request
try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()  # Parse JSON response
    #print("Data:", data["weather"])  # Print the retrieved weather data
    dictprint(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

