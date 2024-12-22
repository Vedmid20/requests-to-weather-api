import requests, os, colorama
from Geocoding import Geocoding
from envData.data import *
from layout.Layout import Layout, title


class CurrentWeather(Layout):
    def __init__(self):
        self.geo = Geocoding()

        self.URL = f'https://api.openweathermap.org/data/2.5/weather'
        self.PARAMS = {'lat': self.geo.lat, 'lon': self.geo.lon, 'appid': TOKEN, 'units': 'metric', 'lang': 'ua', 'cnt': 7}

        self.response = requests.get(self.URL, self.PARAMS)
        self.response.raise_for_status()

    def parsing(self):
        self.weather = f"Weather: {self.response.json()['weather'][0]['main']}\nDescription: {self.response.json()['weather'][0]['description']}"
        self.temperature = (f"\tTemperature: {self.response.json()['main']['temp']} °C\n\tMinimum temperature: {self.response.json()['main']['temp_min']} °C\n"
                            f"\tMaximum temperature: {self.response.json()['main']['temp_max']} °C\n\tFeels like: {self.response.json()['main']['feels_like']} °C\n"
                            f"\tHumidity: {self.response.json()['main']['humidity']}%\n\tPressure: {self.response.json()['main']['pressure']} hPa")
        self.wind = f"\tWind speed: {self.response.json()['wind']['speed']} m/s\n\tWind direction: {self.response.json()['wind']['deg']}°"
        return f'{self.geo.sharp}\n{title("Current Weather")}\n{self.weather}\n{self.temperature}\n{self.wind}\n{self.response.url}'

    def __str__(self):
        return f'{self.response.json()}'
