from ..models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("id", "nickname", "name", "phone", "email", "is_superuser", "is_staff")
        read_only_fields = ("id", "is_superuser", "is_staff")


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("id", "nickname", "name")
