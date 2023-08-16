from rest_framework import serializers

from .author import AuthorShortSerializer
from .genre import GenreSerializer
from  ..models import Book


class BookSerializer(serializers.ModelSerializer):

    author = AuthorShortSerializer()
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = ("title", "publish_year", "genre", "author", "pages_count", "description", "rating")


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "publish_year", "genre", "author", "pages_count", "description")


class BookShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "genre", "author", "rating")
