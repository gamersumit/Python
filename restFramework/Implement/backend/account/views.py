
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework_simplejwt.tokens import AccessToken
from .utils import Utils

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
        # send mail
        status = Utils.sendEmailVerificationLink(request.GET.get('email'), request)
        
        if status[0] :
            return Response({'status': True, 'message' : 'Link Sent Successfully'}, status =200)
        
        if status[1] == 'email not found':
            return Response({'status': False,'message' : 'Email Not Found'}, status = 400)

        else :
            return Response({'status': False,'message' : 'User Already Verified'}, status = 400)

# SHORT NAMING :
user_register_view = RegisterView.as_view()
email_verify_view = EmailVerifyView.as_view()
send_verification_link_view = SendVerificationLinkView.as_view()