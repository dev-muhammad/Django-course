from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..serializers import BookSerializer, BookShortSerializer, BookCreateSerializer
from ..models import Book


class BookApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return BookShortSerializer
        if (self.action == "create"):
            return BookCreateSerializer
        if (self.action == "patch"):
            return BookCreateSerializer
        return BookSerializer
