from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser
import requests



# Create your views here.

class CustomerUserRegistrationView(generics.CreateAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# SHORT NAMING :
user_register_view = CustomerUserRegistrationView.as_view()