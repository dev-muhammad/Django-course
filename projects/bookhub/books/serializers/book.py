from rest_framework import serializers

from .author import AuthorShortSerializer
from .genre import GenreSerializer
from  ..models import Book


class BookSerializer(serializers.ModelSerializer):

    author = AuthorShortSerializer()
    genre = GenreSerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("id", "title", "publish_year", "genre", "author", "pages_count", "description", "rating")

    def get_rating(self, obj):
        return obj.rating or 5

class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "title", "publish_year", "genre", "author", "pages_count", "description")


class BookShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author")
