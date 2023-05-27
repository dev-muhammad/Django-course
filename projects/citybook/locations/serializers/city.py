from rest_framework.serializers import ModelSerializer

from ..models import City
from .country import CountryShortSerializer

class CityShortSerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ["id", "title"]


class CityFullSerializer(ModelSerializer):

    country = CountryShortSerializer()

    class Meta:
        model = City
        fields = ["id", "title", "description", "country", "is_active"]
 