import requests, os, colorama
from Geocoding import Geocoding
from envData.data import *
from layout.Layout import Layout, title, pretty_date


class Forecast(Layout):
    def __init__(self):
        self.geo = Geocoding()

        self.URL = f'https://api.openweathermap.org/data/2.5/forecast'
        self.PARAMS = {'lat': self.geo.lat, 'lon': self.geo.lon, 'appid': TOKEN, 'units': 'metric', 'lang': 'ua', 'cnt': 56}

        self.response = requests.get(self.URL, self.PARAMS)
        self.response.raise_for_status()

    def parsing(self):
        forecast = f"{self.geo.sharp}\n{title('Forecast')}\n"
        for day in self.response.json()['list']:
            date = day['dt_txt']
            weather_main = day['weather'][0]['main']
            weather_description = day['weather'][0]['description']
            temp = day['main']['temp']
            temp_min = day['main']['temp_min']
            temp_max = day['main']['temp_max']
            feels_like = day['main']['feels_like']
            humidity = day['main']['humidity']
            pressure = day['main']['pressure']
            wind_speed = day['wind']['speed']
            wind_deg = day['wind']['deg']

            forecast += (f"\n{pretty_date(date)}\n"
                             f"\tWeather: {weather_main} - {weather_description}\n"
                             f"\tTemperature: {temp} °C\n"
                             f"\tMinimum temperature: {temp_min} °C\n"
                             f"\tMaximum temperature: {temp_max} °C\n"
                             f"\tFeels like: {feels_like} °C\n"
                             f"\tHumidity: {humidity}%\n"
                             f"\tPressure: {pressure} hPa\n"
                             f"\tWind speed: {wind_speed} m/s\n"
                             f"\tWind direction: {wind_deg}°\n")
        return f'{forecast}\n{self.response.url}'
