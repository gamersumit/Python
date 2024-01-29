import requests


endpoint =  "http://127.0.0.1:8000/api/product/"

data = {
    "title": "newFilled as required",
}
get_response = requests.post(endpoint, json = data) # http request

# or
# get_response = requests.get(endpoint)
print(get_response.json())
