import requests


endpoint =  "http://127.0.0.1:8000/api/product/"

data = {
    "title": "Filled as required",
}
get_response = requests.post(endpoint, json = data) # http request
print(get_response.json())
