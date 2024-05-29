import requests


class WeatherService:
    def get_temperature(self, city_name):
        response = requests.get("")
        data = response.json()
        temperature = data.get("temperature")
        return temperature
