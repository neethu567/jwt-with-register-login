from uuid import uuid4

from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from myapp.models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username", "password","c_password"]

    def validate(self, data):
        print("dasdasdas")
        password = data['password']
        c_password = data['c_password']
        if password == c_password:
            print("Success")
            return data

        else:
            print("Check Password")
            raise serializers.ValidationError("Password Wrong")



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name"]

#
# class Loginserializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ["password", "username"]

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False,read_only=True,max_length=5000)

    def validate(self, data):
        username = data.get("username",None)
        password = data.get("password",None)
        if not username and not password:
            raise serializers.ValidationError("Enter data.")

        _user = MyUser.objects.filter(Q(username=username) & Q(password=password)).distinct()

        if not _user.exists():
            raise serializers.ValidationError("Check username or password!")
        # data['token'] = uuid4()
        user = MyUser.objects.get(username=username)

        token = AccessToken.for_user(user)
        # token = "RefreshToken.for_user(user)"
        user.token = token
        user.save()
        return data

    class Meta:
        model = MyUser
        fields = ['username',"password","token"]


