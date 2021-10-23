import pytest
import requests
class TestAPIGetRequests:

    def test_is_redirected(self):
        response = requests.get(
            'https://example.com/api/',
             allow_redirects=True
        )
        assert response.url == 'http://api.example.com'

    def test_base_url_responds(self):
        response = requests.get(
            'https://test3.perksdev.com/api/v1/test',
             allow_redirects=False
        )
        assert response.code == 200