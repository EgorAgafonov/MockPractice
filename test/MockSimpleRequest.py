import requests
from settings import mock_url
import json
import pytest


class TestMockAPI:

    def test_mock_simple_request(self):
        """"""
        headers = {"api_key": "qwerty"}
        request = requests.get(mock_url + '/api/key', headers=headers)
        result = request.json()
        status = request.status_code
        print(status)
        print(type(result))


