from rest_framework.serializers import ModelSerializer

from ..models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ["primary_phone", "secondary_phone", "email", "website"]
