
from rest_framework import serializers
from .models import Link
from user.models import User


class LinkSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model=Link
        fields = "__all__"
    


class CustomUserSerializer(serializers.ModelSerializer):
    shorten_url = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model=User
        fields = [

                "id","name","email","shorten_url"
            ]
