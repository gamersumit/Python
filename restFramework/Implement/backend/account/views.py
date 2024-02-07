
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
# Create your views here.

class RegisterView(generics.GenericAPIView) :
    serializer_class = CustomUserSerializer

    def post(self, request):
        # create a user
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        user = CustomUser.objects.get(email = serializer.data['email'])

        # generate an access token for the user
        token = RefreshToken.for_user(user).access_token

        # absolute url to verify that user
        current_site = str(get_current_site(request))
        relative_link = reverse('email_verify')
        absurl = 'http://'+ current_site + relative_link + "?token=" + str(token)

        # send email to user to verify itself    
        body = f'Hii {user.first_name+" "+user.last_name}\n\nThis email is sent to verify if it\'s you who registered on our djangowebsite.\nTo verify please click on the link below.\n\nVERIFY : {absurl}\n\nThis link is valid only for 1 hour.\nTHANKYOU !!'

        send_mail(
            'Verification mail', 
            body,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False 
            )

        return Response({'status': True, 'data': serializer.data,'message' : 'User Registered Successfully'}, status =200)

class EmailVerifyView(generics.GenericAPIView):

    def get(self, request):
        # fetch token from url
        token = request.GET.get('token')

        try:
            # try to decode token and then get payload attached to the token
            payload = AccessToken(token).payload
            # get usrd id from payload and get user associated with that id
            user = CustomUser.objects.get(id=payload['user_id'])
            
            # check if user is already verified or not
            if not user.is_verified :
                # if not than verify user and return succesful response
                user.is_verified = True
                user.save()
                return Response({"status" : True, "message" : "user verified successfully"}, status = 200)
            # if user is already verfied than send response accordingly
            return Response({"status" : False, "message" : "user already verified"}, status = 400)
        
        # if decoding token fails than handle the response accordingly
        except :
            return Response({"status": False, "message": 'Invalid link or Link Expired'}, status=400)



# SHORT NAMING :
user_register_view = RegisterView.as_view()
email_verify_view = EmailVerifyView.as_view()
