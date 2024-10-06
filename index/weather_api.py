import requests

api_key = 'b05ad82a832f5da790b48645e5943fc7'

# From the name of a city, returns a tuple with its latitud and longitud respectively
def lat_long(name):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={name}&appid={api_key}'
    response = requests.get(url).json()[0]
    lat = response['lat']
    long = response['lon']
    return (lat, long)


# Gathers current climate data from a city taking its latitud and longitud as input
def gather_data_latlong(lat, long):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"
    response = requests.get(url).json()
    return response


# Gathers current climate data from a city taking its name as input. Returb
def gather_data_name(name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}"
    response = requests.get(url).json()
    return response