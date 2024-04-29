from rest_framework import serializers
from . import models as m


class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ['email', 'password']


class RegisterSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = m.User
        fields = BaseUserSerializer.Meta.fields + ['username']


class LoginSerializer(BaseUserSerializer):
    pass
