from rest_framework import serializers

from .genre import GenreSerializer
from  ..models import Author


class AuthorSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "birthdate", "avatar", "genres")


class AuthorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "birthdate", "avatar", "genres")


class AuthorShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "avatar")