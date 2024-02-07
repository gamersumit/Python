
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework_simplejwt.tokens import AccessToken
from .utils import Utils
from django.urls import reverse

# Create your views here.

class RegisterView(generics.GenericAPIView) :
    serializer_class = CustomUserSerializer

    def post(self, request):
        # create a user
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        # send mail
        status = Utils.sendEmailVerificationLink(serializer.data['email'], request)
        
        if status[0] :
            return Response({'status': True, 'data': serializer.data,'message' : 'User Registered Successfully'}, status =200)
        
        if status[1] == 'email not found':
            return Response({'status': False, 'data': "",'message' : 'Email Not Found'}, status = 400)
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

class SendVerificationLinkView(generics.GenericAPIView):
    
    def get(self, request):
        relative_link = reverse('email_verify')
        subject = "Verification Mail  for Django tsting app"
        message = "This email is sent to verify if it\'s you who registered on our djangowebsite.\nTo verify please click on the link below."
        # send mail
        status = Utils.sendLink(request.GET.get('email'), request, relative_link, subject, message)

        if status :
            return Response({'status': True, 'message' : 'Link Sent Successfully'}, status =200)
        
        return Response({'status': False,'message' : 'Email Not Found'}, status = 400)

class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def put(self, request):
        token = request.GET.get('token')

        try:
            # Try to decode the token and get the payload attached to it
            payload = AccessToken(token).payload
            user_id = payload.get('user_id')

            if not user_id:
                raise ValueError("User ID not found in token payload")

            # Get the user associated with the user ID
            user = CustomUser.objects.get(id=user_id)
            

            # Handle resetting the user's password here
        
            serializer = self.serializer_class(user, data = {'password' : request.data.get('password')}, partial=True)
            
            serializer.is_valid(raise_exception = True)
            serializer.save()
            
            return Response({"status": True, "message": "Password reset successfully"}, status=200)
        
        except Exception as e:
            return Response({"status": False, "message": str(e)}, status=400)
        

class SendForgotPasswordLinkView(generics.GenericAPIView):
     def get(self, request):
        print("********************************")

        relative_link = reverse('forgot_password')
        subject = "Password Reset Mail for Django test app"
        message = "To Reset your password please click on the link below."

        # send mail
        status = Utils.sendLink(request.GET.get('email'), request, relative_link, subject, message)
        
        if status :
            return Response({'status': True, 'message' : 'Link Sent Successfully'}, status =200)
        
        
        return Response({'status': False,'message' : 'Email Not Found'}, status = 400)

      

# SHORT NAMING :
user_register_view = RegisterView.as_view()
email_verify_view = EmailVerifyView.as_view()
send_verification_link_view = SendVerificationLinkView.as_view()
forgot_password_view = ForgotPasswordView.as_view()
send_forgot_password_link_view = SendForgotPasswordLinkView.as_view()