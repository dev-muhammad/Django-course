from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


from ..models import CustomUser
from rest_framework import serializers

# login 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class SignUpSerializer(serializers.ModelSerializer):
    
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'token']
        read_only_fields = ('token',)
        extra_kwargs = {'password': {'write_only': True}}
    
    @extend_schema_field(OpenApiTypes.STR)
    def get_token(self, obj):
        return str(obj.auth_token.key)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
class DummySerializer(serializers.Serializer):
    pass
