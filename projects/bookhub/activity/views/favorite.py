from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from .permission import IsOwnerOrReadOnly

from ..serializers import FavoriteCreateSerializer, FavoriteSerializer, FavoriteUpdateSerializer
from ..models import Favorite


class FavoriteApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    permission_classes = [IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Favorite.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return FavoriteSerializer
        if (self.action == "create"):
            return FavoriteCreateSerializer
        if (self.action == "patch"):
            return FavoriteUpdateSerializer
        return FavoriteSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    
    def get_queryset(self):
        if (self.action in ["list", "retrieve"]):
            return Favorite.objects.all().select_related("book") 
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        """
        List of favorite books for authenticated user
        """
        self.queryset = Favorite.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)
