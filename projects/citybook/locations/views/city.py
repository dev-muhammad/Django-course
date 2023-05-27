from rest_framework import mixins, filters
from django_filters import rest_framework as df
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from ..serializers import CityShortSerializer, CityFullSerializer
from ..models import City


class CityViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = City.objects.filter(is_active=True)
    serializer_class = CityShortSerializer
    http_method_names = ['get', 'patch', 'post']

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, df.DjangoFilterBackend]
    search_fields = ['title', 'country__title', 'description']
    ordering_fields = ['title',]
    filterset_fields = ['country']

    def get_permissions(self):
        if self.action in ('create', 'partial_update'):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return CityFullSerializer
        if self.action == 'list':
            return CityShortSerializer
        if self.action == 'retrieve':
            return CityFullSerializer
        return self.serializer_class

