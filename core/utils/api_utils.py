import os
import requests


class ApiUtils:
    def __init__(self, api_key=None):
        self.base_url = os.environ.get("API_BASE_URL")
        self.api_key = api_key

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
        return None

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, data=data, json=json, headers=self._get_headers())
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
        return None

    def put(self, endpoint, data=None, json=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.put(url, data=data, json=json, headers=self._get_headers())
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
        return None

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.delete(url, headers=self._get_headers())
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
        return None

    def _get_headers(self):
        headers = {'Content-Type': 'application/json'}
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
        return headers
