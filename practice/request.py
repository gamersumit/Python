# Request library in python
# task given on 18-1

################################
#pipenv install requests   
 
import requests  # importing request module to get its functionality and dependencies
from requests.exceptions import HTTPError # importing httperror module from requests excetions to identify http errors
import json   # to work with request's response as json object

try:
    response = requests.get('https://v2.jokeapi.dev/joke/Any') # trying to retrieve data(instance of response) and storing it in a variable named response

except HTTPError as http_err:  # check if any HTTP error HAS OCCURED
    print(f'HTTP error occurred: {http_err}')  

except Exception as e:      # CHECK IF ANY OTHER ERROR HAS OCCURED
    print(f'Other error occurred: {e}')

else:  # if no exception/error occurs/ if our request is successful
    print('status code: ', {response.status_code} )  # it will print status code for our resquest indicates what happened with our request
    dic = response.json()  # converting information recevied in response of our request to python dictionary using .json() mwthod

    if dic.get('category') :   # extrecting information from dictionary we just received
        print(f"category: {dic.get('category')}")  # print value of category if exists

    if dic.get('type') : 
        print(f"type: {dic.get('type')}")  # print value of type if exists

    if dic.get('setup') :
        print(f"setup: {dic.get('setup')}") #print value of setup if exists

    if dic.get('delivery') :
        print(f"delivery: {dic.get('delivery') }") # printcalue of delivery if exists



