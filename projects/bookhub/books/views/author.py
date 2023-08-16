from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import AuthorSerializer, AuthorCreateSerializer
from ..models import Author


class AuthorApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if (self.action == "create"):
            return AuthorCreateSerializer
        if (self.action == "patch"):
            return AuthorCreateSerializer
        return AuthorSerializer
