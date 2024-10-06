import requests

def coordsearch_dict(data):
    for key, value in data.items():
        if isinstance(value, list) or isinstance(value, dict):
            if isinstance(value, dict):
                coordsearch_dict(value)
            else:
                coordsearch_list(value)
        else:
            if key == "lat":
                global globalx
                globalx = value
            if key == "lon":
                global globaly
                globaly = value
def coordsearch_list(data):
    x = 0
    y = 0
    for i in data:
        if isinstance(i, dict):
            coordsearch_dict(i)
        elif isinstance(i, list):
            coordsearch_list(i)
        else:
            pass
    return (x,y)
def listprint(data):
    for i in data:
        print(i)
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
            if isinstance(value, dict):
                dictprint(value)
            else:
                listprint(value)
        else:
            print(f"{key}: {value}")  # Print the individual value

def lat_long(s):
    api_key = "b05ad82a832f5da790b48645e5943fc7"
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={s}&limit=5&appid={api_key}'
    response = requests.get(url).json()[0]
    lat = response['lat']
    long = response['lon']
    return (lat, long)
def coordfetch():
    url = "http://api.openweathermap.org/geo/1.0/direct"
    api_key = "b05ad82a832f5da790b48645e5943fc7"
    s = "mexicali"
    globalx = 0
    globaly = 0
    cosa = {
    "appid": api_key,   # Include your API key
    "q": s,
    "limit": 5
    }
    try:
        response = requests.get(url, params=cosa)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse JSON response
        listprint(data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    print(globalx,globaly)
def climatefetch_coord(lat_long):
    api_key = "b05ad82a832f5da790b48645e5943fc7"
    url2 = "https://api.openweathermap.org/data/2.5/weather"
    params_coord = {
    "appid": api_key,   # Include your API key
    "lon": lat_long[1],
    "lat": lat_long[0],
    "limit": 5
    #"q": s
    }
    if lat_long[0] == 0 and lat_long[1] == 0:
        print("Tu papa en 3d")
    else:
        try:
            response = requests.get(url2, params=params_coord)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()  # Parse JSON response
            #print("Data:", data["weather"])  # Print the retrieved weather data
            dictprint(data)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
def climatefetch_name(s):
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "b05ad82a832f5da790b48645e5943fc7"
    params = {
        "appid": api_key,   # Include your API key
        "q": s,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse JSON response
        #print("Data:", data["weather"])  # Print the retrieved weather data
        dictprint(data)
        return True
    except requests.exceptions.RequestException as e:
        return False
def name_check(s):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    api_key = "b05ad82a832f5da790b48645e5943fc7"
    params = {
        "appid": api_key,   # Include your API key
        "q": s,
        "limit": 100
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse JSON response
        for i in data:
            print(i["name"], i["country"], i["lat"], i["lon"])
        j = int(input("n: ")) -1
        print(data[j]["name"], data[j]["country"], j)
        return(data[j]["name"])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
def decision(): 
    s = input("Place: ")
    s = name_check(s)
    if not climatefetch_name(s):
        climatefetch_coord(lat_long(s))

decision()
