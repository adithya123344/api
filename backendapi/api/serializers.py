from distutils.file_util import write_file
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . models import deskStatus
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only': True,'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=deskStatus
        fields='__all__'