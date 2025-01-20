import requests
import json

def getWeather():

    with open("config.json") as config_file:
        config = json.load(config_file)

    WEATHER_API_KEY = config.get("WEATHER_API_KEY")

    API_KEY = WEATHER_API_KEY
    city = "Baltimore"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,#add or remove & idk bro its weird
        "units": "imperial"  # use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        
        return f"City: {data['name']} Temperature: {data['main']['temp']} °F Weather: {data['weather'][0]['description']}"
    else:
        return f"Error: {response.status_code}"
        
