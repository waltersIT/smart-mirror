import requests
import json

def getWeather():

    API_KEY = "YOUR API KEY"
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
        
