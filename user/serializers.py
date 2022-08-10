from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class RegisterSerializer(RegisterSerializer):
    name = serializers.CharField()
