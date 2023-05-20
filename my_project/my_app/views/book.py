from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from my_app.models import Book
from my_app.serializers import BookSerializer, BookShortSerializer, BookCreateSerializer

class BookViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    # queryset = Book.objects.all()
    queryset = Book.objects.select_related('author', 'author__contacts').prefetch_related('categories')

    # serializer_class = BookSerializer
    
    def get_serializer_class(self):
        if self.action == "create":
            return BookCreateSerializer
        return BookSerializer




class Book1ViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookShortSerializer

    def list(self, request, *args, **kwargs):
        print("list")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("retrieve")
        return super().retrieve(request, *args, **kwargs)

    


