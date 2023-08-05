from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from ..serializers import BookSerializer, BookListSerializer, BookCreateSerializer, BookUpdateSerializer
from ..models import Book

class BookGenericApiView(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin
    ):

    permission_classes = [AllowAny]
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return BookListSerializer
        if (self.action == "create"):
            return BookCreateSerializer
        if (self.action == "patch"):
            return BookUpdateSerializer
        return BookSerializer
