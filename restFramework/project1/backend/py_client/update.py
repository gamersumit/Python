import requests


endpoint =  "http://127.0.0.1:8000/api/product/3/update/"

data = {
    'title': 'updated title',
    'content': 'title is updated',
    'price': 458,
}
get_response = requests.put(endpoint, json=data) # http request
print(get_response.json())
