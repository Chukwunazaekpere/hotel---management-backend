from rest_framework import serializers
from .models import Users

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'email', 'password', 'confirm_password']

    