import pytest
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


def auth_token():
    #     {
#   "email": "customer@practicesoftwaretesting.com",
#   "password": "welcome01"
# }
    client_id = 'customer@practicesoftwaretesting.com'
    client_secret = 'welcome01'

    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='http://localhost:8091/oauth2/token', client_id=client_id,
                              client_secret=client_secret, auth=auth)
    print(f'test {token}')
    print ("test")