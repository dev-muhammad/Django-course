from ..models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("pk", "nickname", "name", "phone", "email", "is_superuser", "is_staff")
        read_only_fields = ("pk", "is_superuser", "is_staff")
