from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from ..serializers import PlaceShortSerializer, PlaceFullSerializer
from ..models import Place


class PlaceViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Place.objects.filter(is_active=True)
    serializer_class = PlaceShortSerializer
    http_method_names = ['get', 'patch', 'post']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name',]

    def get_permissions(self):
        if self.action in ('create', 'partial_update'):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return PlaceFullSerializer
        if self.action == 'list':
            return PlaceShortSerializer
        if self.action == 'retrieve':
            return PlaceFullSerializer
        if self.action == 'subcategories':
            return PlaceFullSerializer
        return self.serializer_class
    
    @action(detail=True, methods=["get"], url_path="subcategories")
    def subcategories(self, request, *args, **kwargs):
        """
        Get subcategories

        From this endpoint you can get all subategories by parent categor id
        """
        category: Place = self.get_object()
        self.queryset = category.subcategories.filter(is_active=True)
        return super().list(request, *args, **kwargs)
