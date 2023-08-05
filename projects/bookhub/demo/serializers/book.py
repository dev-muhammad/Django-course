from rest_framework import serializers

from ..models import Book
from .author import AuthorSerializer
from  .category import CategorySerializer


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Book
        fields = ['id', "name", "author", "categories", "publish_year", "publisher", "description", "pages", "is_active"]
        # fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', "name",  "description", "pages"]


class BookCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', "name", "author", "categories", "description", "pages", "publish_year", "publisher"]


class BookUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ["name", "categories", "description", "publish_year"]

