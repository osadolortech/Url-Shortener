from wsgiref.validate import validator
from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class RegisterSerializer(RegisterSerializer):
    name = serializers.CharField()
