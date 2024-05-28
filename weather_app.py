import json.decoder

import requests


class WeatherService:
    """"""

    def get_temperature(self, city_name):

        response = requests.get(f"адрес мок-сервера")
        data = response.json()
        temperature = data.get("temperature")

        return temperature
