from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from my_app.models import Book
from my_app.serializers import BookSerializer, BookShortSerializer, BookCreateSerializer, AuthorSerializer, CategorySerializer, CategoryFullSerializer

class MyBookViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):

    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookShortSerializer

    def get_queryset(self):
        # if self.action == "categories":
        #     #book = self.get_object()
        #     r = Book.objects.get(pk=self.kwargs[self.lookup_field]).categories.all()
        #     print(r)
        #     return r #Book.objects.all()
        return super().get_queryset()
    
    # def get_serializer(self, *args, **kwargs):
    #     if self.action == "create":
    #         return BookCreateSerializer
    #     return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = BookCreateSerializer
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result = serializer.data
        result["key"] = 12
        return Response(result)
    
    @action(detail=True, methods=["get"], url_path="author")
    def author(self, request, *args, **kwargs):
        book = self.get_object()
        result = AuthorSerializer(book.author)
        return Response(data=result.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["get"], url_path="categories")
    def categories(self, request, *args, **kwargs):
        book = self.get_object()
        self.queryset = book.categories.all()
        self.serializer_class = CategoryFullSerializer
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=["get"], url_path="count")
    def count(self, request, *args, **kwargs):
        count = self.queryset.count()
        result = {"count": count}
        return Response(data=result, status=status.HTTP_200_OK)
    



