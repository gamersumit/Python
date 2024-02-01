import requests
from getpass import getpass



auth_endpoint =  "http://127.0.0.1:8000/api/auth/"
# jwt_token_obtain_endpoint = "http://127.0.0.1:8000/api/token/"
# jwt_token_refresh_endpoint = "http://127.0.0.1:8000/api/token/refresh/"
# jwt_token_verify_endpoint = "http://127.0.0.1:8000/api/token/verify/"

# token = JwtToken.jwt_tokens

# if token :
#     headers = {
#         # 'Authorization' : f"Token {token}" # default keyword is token
#         'Authorization' : f"Bearer {token}" # custom name for token is bearer
#     }
#     response = requests.post(jwt_token_verify_endpoint, headers = headers)
#     print(response.json(), "verified")

# else :
#     username = input("Username: ")
#     password = getpass()  # take input and encrypted password
#     response = requests.post(jwt_token_obtain_endpoint, json = {'username' : username, 'password' : password}) # http request
#     print(response.json(), "obtained")


username = input("Username: ")
password = getpass()  # take input and encrypted password

auth_response = requests.post(auth_endpoint, json = {'username' : username, 'password' : password}) # http request
print(auth_response.json())


if auth_response.status_code == 200 :
    token = auth_response.json()['token']
    headers = {
        # 'Authorization' : f"Token {token}" # default keyword is token
        'Authorization' : f"Bearer {token}" # custom name for token is bearer
    }
    endpoint =  "http://127.0.0.1:8000/api/product/list/"

    get_response = requests.get(endpoint, headers = headers, ) # http request
    print(get_response.json())
