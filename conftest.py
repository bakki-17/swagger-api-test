import pytest
import requests
import json
from utils.APIClient import APICLIENT
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


@pytest.fixture
def api():
    return APICLIENT()

# @pytest.fixture
# def auth_token():
#     loginURL = 'http://localhost:8091/users/login'    
#     payload = {"email": "customer@practicesoftwaretesting.com",
#       "password": "welcome01"}

#     login = requests.post(loginURL, payload)
#     jsonResp = login.json()
#     token = json.dumps(jsonResp["access_token"])

#     return token