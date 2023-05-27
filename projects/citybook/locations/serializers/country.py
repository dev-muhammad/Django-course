from rest_framework.serializers import ModelSerializer

from ..models import Country


class CountryShortSerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ["id", "title"]


class CountryFullSerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ["id", "title", "description", "is_active"]
 