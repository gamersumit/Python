from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
import re

class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length = 8, write_only = True)
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_mode_user',
            'is_master_user',
            'is_verified',
        ]
    
    
    
    def validate_password(self, value):
        # valid password : >= 8 char, must contains lower at least 1 char of each 
        # lower(alpha), upper(alpha), (number), (symbols)
       

        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        if  not re.search("\d", value) :
            raise serializers.ValidationError("Password must contains a number 0 to 9")
        
        if not re.search("[a-z]", value) :
            raise serializers.ValidationError("Password must contain a lowercase letter ")
        
        if not re.search("[A-Z]", value) :
            raise serializers.ValidationError("Password must contain a uppercase letter")
        
        if not re.search(r"[@#$%^&*()\-_+=.]", value):
            raise serializers.ValidationError("Password must contain a special character(@,#,$,%,^,&,*,(,),-,_,+,=,.)")

        return make_password(value)    # return hashed password
    

    # def validate_email(self, value):
    #     pass

    
    
    