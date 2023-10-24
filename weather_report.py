import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "65fb52a6635ff72d10951f4eeb7d4b15"
CITY = "New delhi"

def kelvin_to_celsius(kelvin):
    celsius =kelvin - 273


    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
wind_speed = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_celsius:.2f} degree Celsius")
print(f"wind speed in {CITY}: {wind_speed}m/s")