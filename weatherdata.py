from typing import Literal
import requests, json
from urllib import request
import urllib.request
import csv

# api_key = INPUT YOUR API KEY FROM www.openweathermap.org
# locationname = INPUT YOUR LOCATION AS STRING

url_location = "http://api.open-notify.org/iss-now.json"
api_call_location = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(locationname, api_key)

iss_recordings = []


def get_ISS_weather(lat, lon):
    api_call_latlong = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, api_key)

    # json repsonse
    json_data = requests.get(api_call_latlong).json()

    # get location data
    
    location_data = {
        'lat' : lat,
        'lon' : lon,
        'city' : json_data['name'],
        'country' : json_data['sys']
    }

    # get weather data
    weather_data  = {
        'weather_main' : json_data['weather'][0]['main'],
        'weather_description' : json_data['weather'][0]['description'],
        'temp': round(json_data['main']['temp']-273.15, 2),
        'pressure' : json_data['main']['pressure'],
        'humidity' : json_data['main']['humidity'],
        'windspeed' : json_data['wind']['speed'],
        'winddirection' : json_data['wind']['deg'],
        'cloudcover' : json_data['clouds']['all']
    }

    data ={
        'position' : location_data,
        'weather_data' : weather_data
    }

    return data

def ISS_data_writer(wdata):
    lat = wdata['position']['lat']
    lon = wdata['position']['lon']
    temp = wdata['weather_data']['temp']
    press = wdata['weather_data']['pressure']
    hum = wdata['weather_data']['humidity']
    ws = wdata['weather_data']['windspeed']

    with open('weather.csv', mode='a', newline="") as wfile:
        writer = csv.writer(wfile, delimiter=',', quotechar='"')
        writer.writerow([lat, lon, temp, press, hum, ws])


while True: 
    # get ISS location
    response_iss = urllib.request.urlopen(url_location)
    result_iss = json.loads(response_iss.read())
    location = result_iss['iss_position']
    lon = float(location['longitude'])
    lat = float(location['latitude'])

    
    # get weather data
    iss_data = get_ISS_weather(lat,lon)
    ISS_data_writer(iss_data)
    print(iss_data)
