from rest_framework.serializers import ModelSerializer

from ..models import Place
from .contact import ContactSerializer
from .gps_location import GpsLocationSerializer
from .working_hours import WorkingHoursSerializer
from .photo import PhotoSerializer
from locations.serializers import CityShortSerializer
from categories.serializers import CategoryShortSerializer

class PlaceShortSerializer(ModelSerializer):

    class Meta:
        model = Place
        fields = ["title", "description"]


class PlaceFullSerializer(ModelSerializer):

    
    category = CategoryShortSerializer()
    city = CityShortSerializer()
    contacts = ContactSerializer()
    gps_location = GpsLocationSerializer()
    working_hours = WorkingHoursSerializer(many=True)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Place
        fields = ["title", "description", "category", "address", "city", "contacts", "gps_location", "working_hours", "photos"]
