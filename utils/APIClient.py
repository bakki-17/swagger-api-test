import yaml
import requests
from auth import auth_headers
# from requests.auth import HTTPBasicAuth

class APICLIENT:
    def __init__(self):
        with open("utils/config.yaml", 'r') as file:
            config = yaml.safe_load(file)
            self.baseURL = config["BASE_URL"]
            self.endpoints = config["endpoints"]
        
        # self.baseURL = BASE_URL
        self.headers = auth_headers
        # self.login = loginURL
        # self.loginPayload = payload

    def postRequest(self, endpoint_key, endpoint_path='', data=None):
        url = f"{self.baseURL}{self.endpoints[endpoint_key]}{endpoint_path}"
        response = requests.post(url, headers=self.headers, json=data)
        return response
    
    def getRequest(self, endpoint_key, endpoint_path='', params=None):
        url = f"{self.baseURL}{self.endpoints[endpoint_key]}{endpoint_path}"
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def updateRequest(self, endpoint, data=None):
        url = f"{self.baseURL}{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        return response
    
    def deleteRequest(self, endpoint):
        url = f"{self.baseURL}{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response