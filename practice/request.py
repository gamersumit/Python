# Request library in python
# task given on 18-1

################################
#pipenv install requests   
 
import requests  # importing request module to get its functionality and dependencies
from requests.exceptions import HTTPError # importing httperror module from requests exceptions to identify http errors
import json   # to work with request's response as json object

response = requests.get('https://v2.jokeapi.dev/joke/Any') # trying to retrieve data(instance of response) and storing it in a variable named response
 
if(response.status_code != 200) : # check if any HTTP error HAS OCCURED during the excution of code (request for retriving data)
    print(f'HTTP error occurred')  

else:  # if no exception/error occurs/ if our request is successful
    print('status code: ', {response.status_code} )  # it will print status code for our resquest indicates what happened with our request
    dic = response.json()  # converting information recevied in response of our request to python dictionary using .json() mwthod

    if dic.get('category') :   # extrecting information from dictionary we just received
        print(f"category: {dic.get('category')}")  # print value of category if exists

    if dic.get('setup') :
        print(f"setup: {dic.get('setup')}") #print value of setup if exists

    if dic.get('delivery') :
        print(f"delivery: {dic.get('delivery') }") # print value of delivery if exists

    if dic.get('type') : 
        print(f"type: {dic.get('type')}")  # print value of type if exists

    print("****************************************************************\n")
    print(" JOKE:\n\n",dic.get('setup'),"\n",dic.get('delivery'))
    print("\n****************************************************************")




