from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

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

    def create(self, validated_data):
        print("create")
        validated_data['password'] = make_password(validated_data.get('password'))
        print(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user