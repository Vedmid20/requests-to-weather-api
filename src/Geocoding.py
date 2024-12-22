import requests, os, colorama
from envData.data import *


class Geocoding:
    def __init__(self):
        self.URL = f'http://api.openweathermap.org/geo/1.0/direct'
        self.PARAMS = {'q': [CITY, STATE, COUNTRY_CODE], 'limit': LIMIT, 'appid': TOKEN}
        self.response = requests.get(self.URL, self.PARAMS)
        self.response.raise_for_status()
        self.sharp = f'{colorama.Fore.LIGHTBLACK_EX + '#' * 250 + colorama.Style.RESET_ALL}'
        self.lat = self.response.json()[0]['lat']
        self.lon = self.response.json()[0]['lon']

    def get_cord(self):
        return f'Lat: {self.lat}, Lon: {self.lon}'

    def __str__(self):
        return f'{self.sharp}\n{self.response.json()}\n{self.response.url}\n{self.sharp}'
