from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from ..serializers import BookSerializer, BookShortSerializer, BookCreateSerializer
from ..models import Book
from activity.serializers import ReviewBookSerializer


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
            return BookSerializer
        if (self.action == "create"):
            return BookCreateSerializer
        if (self.action == "patch"):
            return BookCreateSerializer
        if (self.action == "reviews"):
            return ReviewBookSerializer
        return BookSerializer
    
    def get_queryset(self):
        if (self.action in ["list", "retrieve"]):
            return Book.objects.all().select_related("author", "genre") 
        return super().get_queryset()

    @action(detail=True, methods=["get"], url_path="reviews")
    def reviews(self, request, *args, **kwargs):
        """
        Get reviews of book
        """
        self.queryset = self.get_object().reviews.select_related("user")
        return super().list(request, *args, **kwargs)