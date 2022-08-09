from dataclasses import fields
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

class RegisterSerializer(RegisterSerializer):
    name = serializers.CharField()

