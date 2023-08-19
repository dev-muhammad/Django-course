from rest_framework import serializers

from books.serializers import BookShortSerializer
from  ..models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):

    book = BookShortSerializer()

    class Meta:
        model = Favorite
        fields = ("id", "book", "status", "status_text", "create_time")


class FavoriteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ("id", "user", "book", "status", "status_text", "create_time")
        read_only_fields = ("user", "status_text", "create_time")

    def create(self, validated_data):
        validated_data["user"] = self.context["user"]
        return super().create(validated_data)


class FavoriteUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ("id", "user", "book", "status","status_text", "create_time")
        read_only_fields = ("user", "book", "status_text", "create_time")

