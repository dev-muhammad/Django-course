from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import BookSerializer, BookListSerializer, BookCreateSerializer, BookUpdateSerializer, AuthorSerializer, CategorySerializer
from ..models import Book, Category, Author

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
        if (self.action in  ["categories", "all_categories"]):
            return CategorySerializer
        if (self.action == "authors"):
            return AuthorSerializer
        return BookSerializer

    @action(detail=True, methods=["get"], url_path="author")
    def author(self, request, *args, **kwargs):
        """
        Get author of book
        """
        book: Book = self.get_object()
        data = AuthorSerializer(book.author).data
        return Response(data=data)

    @action(detail=True, methods=["get"], url_path="categories")
    def categories(self, request, *args, **kwargs):
        """
        Get categories of book
        """
        book: Book = self.get_object()
        self.queryset = book.categories.all()
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=["get"], url_path="categories")
    def all_categories(self, request, *args, **kwargs):
        """
        Get all categories of book
        """
        self.queryset = Category.objects.all()
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=["get"], url_path="authors")
    def authors(self, request, *args, **kwargs):
        """
        Get all authors of book
        """
        self.queryset = Author.objects.all()
        return super().list(request, *args, **kwargs)
