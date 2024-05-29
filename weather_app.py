import requests


class WeatherService:
    def get_temperature(self, city_name):
        response = requests.get("https://f6b92c67-cfe4-4fd4-8084-e2e5efa9d5c9.mock.pstmn.io/weather")
        data = response.json()
        temperature = data.get("temperature")
        return temperature
