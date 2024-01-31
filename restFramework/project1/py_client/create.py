import requests


endpoint =  "http://127.0.0.1:8000/api/product/create/"
title = input("enter title")

data = {
    "title": "mixin implemented properly",
    'price': 348,
}
get_response = requests.post(endpoint, json = data) # http request
print(get_response.json())
