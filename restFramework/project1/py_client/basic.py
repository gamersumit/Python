import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org"
endpoint="https://httpbin.org/anything" # rest api

get_response = requests.get(endpoint) # http request
print(get_response.text) # print raw text response


# HTTP REQUEST -> HTML
# REST API HTTP REQUEST -> JSON(xml)
print(get_response.json()) #python dictionary -- only works if get_response is a json object (response of rest api http request)