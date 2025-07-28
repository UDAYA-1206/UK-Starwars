# lib/swapi_client.py
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SWAPIClient:
    def __init__(self):
        self.session = requests.Session()

    def get_json(self, url):
        return self.session.get(url, verify=False).json()

    def get_movies(self, api_base):
        return self.get_json(f"{api_base}/films/")["results"]
