from rest_framework.serializers import ModelSerializer

from ..models import GpsLocation


class GpsLocationSerializer(ModelSerializer):

    class Meta:
        model = GpsLocation
        fields = ["lat", "lon"]
