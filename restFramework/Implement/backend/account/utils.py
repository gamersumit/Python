from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
class Utils :

    @staticmethod
    def sendEmailVerificationLink(email, request) :
        # from email fetch user
        print(email)
        try :
            user = CustomUser.objects.get(email = email)
        
        # if email not found or user is already verified
        except :
            return (False, 'email not found')
        
        else :        
            if user.is_verified : 
                return (False, 'user is already verified')
        
            # else
            # generate an access token for the user
            token = RefreshToken.for_user(user).access_token

            # absolute url to verify that user
            current_site = str(get_current_site(request))
            relative_link = reverse('email_verify')
            absurl = 'http://'+ current_site + relative_link + "?token=" + str(token)

            # send email to user to verify itself    
            body = f'Hii {user.first_name+" "+user.last_name}\n\nThis email is sent to verify if it\'s you who registered on our djangowebsite.\nTo verify please click on the link below.\n\nVERIFY : {absurl}\n\nThis link is valid only for 1 hour.\nTHANKYOU !!'

            send_mail(
                'Verification mail for Django test web app', 
                body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False 
                )
            
            return (True, 'email sent successfully')