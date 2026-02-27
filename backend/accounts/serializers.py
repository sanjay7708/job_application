from rest_framework import serializers
from django.contrib.auth.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password','confirm_password']
    def validate(self, data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError('password does not match')
        return data
    def create(self,validated_data):
        validated_data.pop('confirm_password')
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user
    