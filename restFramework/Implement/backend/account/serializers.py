from rest_framework import serializers
from .models import CustomUser
from .utils import Utils

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
       return Utils.validate_password(value)
    

class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length = 8, write_only = True)
    class Meta:
        model = CustomUser
        fields = ['password']
    
    def validate_password(self, value):
       return Utils.validate_password(value)
    