from rest_framework import serializers
from django.contrib.auth.models import User
from WebSite.models import *

# class SingupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'first_name', 'last_name', 'email')


class salebascket(serializers.ModelSerializer):
    class Meta:
        model = salebascket
        fields = '__all__'


