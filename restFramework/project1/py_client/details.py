import requests


endpoint =  "http://127.0.0.1:8000/api/product/1"


get_response = requests.get(endpoint, params = {"abc": 123}, json={"title" :"titiled", "content": "hello world"}) # http request
print(get_response.json())
