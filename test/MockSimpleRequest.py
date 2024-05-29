import requests
import json
import pytest


class TestMockAPI:

    def test_mock_simple_request(self):
        """"""

        request = requests.get("https://e2a64595-8bb4-4475-9cf3-cc189ea65fbc.mock.pstmn.io/user_id")
        result = request.json()
        status = request.status_code
        print(status)
        print(result['user_id'])


