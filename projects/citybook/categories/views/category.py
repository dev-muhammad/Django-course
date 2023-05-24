from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from ..serializers import *
from ..models import Category


class CategoryViewSet(GenericViewSet,
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin
                    ):
    
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryShortSerializer
    #permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'post']

    def get_permissions(self):
        if self.action in ('create', 'partial_update'):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return CategoryCreateSerializer
        if self.action == 'list':
            return CategoryShortSerializer
        if self.action == 'retrieve':
            return CategoryFullSerializer
        if self.action == 'subcategories':
            return CategoryChildsSerializer
        return self.serializer_class
    
    @action(detail=True, methods=["get"], url_path="subcategories")
    def subcategories(self, request, *args, **kwargs):
        """
        Get subcategories

        From this endpoint you can get all subategories by parent categor id
        """
        category: Category = self.get_object()
        self.queryset = category.subcategories.filter(is_active=True)
        return super().list(request, *args, **kwargs)
