import requests
from getpass import getpass

auth_endpoint =  "http://127.0.0.1:8000/api/auth/"
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

    get_response = requests.get(endpoint, headers = headers) # http request
    print(get_response.json())
