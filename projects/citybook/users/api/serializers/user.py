from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ("pk", "username", "first_name", "last_name", "email", "is_superuser", "is_staff")
        read_only_fields = ("pk", "is_superuser", "is_staff")
