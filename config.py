
# import json
# import requests

# """"
# Login to get the access_token
# """

# loginURL = 'http://localhost:8091/users/login'    
# payload = {
#         "email": "customer@practicesoftwaretesting.com",
#         "password": "welcome01"
#         }
# login = requests.post(loginURL, payload)
# jsonResp = login.json()
# tokenResp = json.dumps(jsonResp["access_token"])
# tokenType = json.dumps(jsonResp["token_type"])

# accessToken = str(tokenType).strip('"') + " " + str(tokenResp).strip('"')

# auth_headers = {
#     "Authorization" : accessToken,
#     "Content-type" : "applicaiton/json",
#     "Accept" : "application/json"
# }



