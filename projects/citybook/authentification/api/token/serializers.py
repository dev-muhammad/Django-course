from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from django.contrib.auth import get_user_model
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class SignUpSerializer(serializers.ModelSerializer):
    
    token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'token']
        read_only_fields = ('token',)
        extra_kwargs = {'password': {'write_only': True}}
    
    @extend_schema_field(OpenApiTypes.STR)
    def get_token(self, obj):
        return str(obj.auth_token.key)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
class DummySerializer(serializers.Serializer):
    pass