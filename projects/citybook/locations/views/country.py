from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from ..serializers import CountryShortSerializer, CountryFullSerializer, CityShortSerializer
from ..models import Country


class CountryViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountryShortSerializer
    http_method_names = ['get', 'patch', 'post']

    def get_permissions(self):
        if self.action in ('create', 'partial_update'):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return CountryFullSerializer
        if self.action == 'list':
            return CountryShortSerializer
        if self.action == 'retrieve':
            return CountryFullSerializer
        if self.action == 'cities':
            return CityShortSerializer
        return self.serializer_class
    
    @action(detail=True, methods=["get"], url_path="cities")
    def cities(self, request, *args, **kwargs):
        """
        Get cities

        From this endpoint you can get all cities of country
        """
        country: Country = self.get_object()
        self.queryset = country.cities.filter(is_active=True)
        return super().list(request, *args, **kwargs)
