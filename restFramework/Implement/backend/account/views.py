from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser
import requests
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

class CustomUserRegistrationView(generics.CreateAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class SendMail(APIView) :
    def post(self,request):

        email = request.data.get('to')
        if not email:
            return Response({'status': False, 'message': 'Missing recipient email'}, status=400)
      
        emailw = EmailMessage(
            'testing subject', 
            'testing email body, this message is from python',
            settings.EMAIL_HOST_USER,
            [email] 
        )

        try :
            emailw.send(fail_silently=False)
            return Response({'status' : True, 'message' : 'Email sent successfully'})
        
        except Exception as e:
            return Response({'status' : False, 'message' : str(e)}, status = 500)



# SHORT NAMING :
user_register_view = CustomUserRegistrationView.as_view()
