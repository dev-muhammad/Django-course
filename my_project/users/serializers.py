from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "nickname", "email", "phone", "gender", "name", "bio", "password", "is_active")
        extra_kwargs = {'password': {'write_only': True}}

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "nickname", "email", "phone", "gender", "name", "bio", "password")
        extra_kwargs = {'password': {'write_only': True}, 'nickname': {'write_only': True}}



from rest_framework.authtoken.serializers import AuthTokenSerializer

class CustomAuthTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        # Get the nickname value from the request data
        nickname = attrs.get('nickname')
        if nickname:
            # Update the attrs dictionary to use 'nickname' instead of 'username'
            attrs['username'] = nickname
            del attrs['nickname']
        return super().validate(attrs)