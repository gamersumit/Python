from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
import re

class CustomUserSerializer(serializers.ModelSerializer):

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

        return value



    def create(self, validated_data):
        print("create")
        validated_data['password'] = make_password(validated_data.get('password'))
        print(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user
    
    
    