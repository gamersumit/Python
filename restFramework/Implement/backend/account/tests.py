from django.test import TestCase
from .models import *
from rest_framework.test import APITestCase
from faker import Faker
fake = Faker()
import json

# Create your tests here.

class AccountTest(APITestCase):

    # def test_RegisterView(self):
    #     _data = {
    #         "first_name": "sumit",
    #         "last_name": "aggarwal",
    #         "username": "claw",
    #         "password": "Owner@1234",
    #         "email": "test@example.com",
            
    #     }

    #     _response = self.client.post('/account/register/', data = _data, format = 'json')
    #     _data = _response.json()
    #     self.assertEqual(_response.status_code, 200)


    def test_LoginView(self):
        _data = {
            "first_name": "sumit",
            "last_name": "aggarwal",
            "username": "claw",
            "password": "Owner@1234",
            "email": "test@example.com",
            
        }

        _response = self.client.post('/account/register/', data = _data, format = 'json')
        _data = _response.json()
    
        self.assertEqual(_response.status_code, 200)


        _data = {
            "password": "Owner@1234",
            "email": "test@example.com",
        }
         
        json_data = json.dumps(_data)
        
        _response = self.client.post('/account/login/', data=json_data, content_type='application/json')
        _data = _response.json()
        self.assertEqual(_response.data['message'],'g')


   