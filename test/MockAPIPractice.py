import requests
from settings import mock_url
import json
import pytest


class TestMockAPI:

    def test_mock_simple_request(self):
        """"""

        request = requests.get(mock_url)
        result = request.json()
        status = request.status_code
        print(status)
        print(result['user_id'])