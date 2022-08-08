from wsgiref.validate import validator
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField(required=True,write_only=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required= True,write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required= True,write_only=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "password filed didnt match"})
        return attrs
