import requests
from settings import mock_url
import json
import pytest


class TestMockAPI:

    def test_mock_request_apikey(self):
        """"""

        headers = {"api_key": "qwerty"}
        request = requests.get(mock_url + '/api/key', headers=headers)
        result = request.json()
        status = request.status_code
        print(f"\n{result}")

        assert status == 200
        assert len(result["key"]) >= 7

    def test_mock_request_userid(self):
        """"""

        headers = {"api_key": "qwerty"}
        request = requests.get(mock_url + '/users', headers=headers)
        result = request.json()
        status = request.status_code
        print(f"\n{result}")

        assert status == 200
        assert str(result["user_id"]).isdigit



