import requests

BASE_URL = 'https://api.mailcheck.ai'

class MailCheckClient:
    def __init__(self, api_key=""):
        self._headers = {}

        if api_key != '':
            self._headers = {'Authorization': f'Bearer {api_key}'}

    def _make_request(self, endpoint):
        url = f'{BASE_URL}/{endpoint}'
        return requests.get(url, headers=self._headers).json()

    def check_domain(self, domain):
        endpoint = f'domain/{domain}'
        return self._make_request(endpoint)
        
    def check_email(self, email):
        endpoint = f'email/{email}'
        return self._make_request(endpoint)
