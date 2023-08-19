from rest_framework import serializers

from books.serializers import BookShortSerializer
from users.serilizers import UserShortSerializer
from  ..models import Review


class ReviewBookSerializer(serializers.ModelSerializer):

    user = UserShortSerializer()

    class Meta:
        model = Review
        fields = ("id", "user", "rate", "description", "create_time")


class ReviewUserSerializer(serializers.ModelSerializer):

    book = BookShortSerializer()

    class Meta:
        model = Review
        fields = ("id", "book", "rate", "description", "create_time")


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("id", "book", "rate", "description")
    
    def create(self, validated_data):
        validated_data["user"] = self.context["user"]
        return super().create(validated_data)


class ReviewUpdateSerializer(serializers.ModelSerializer):

    book = BookShortSerializer()

    class Meta:
        model = Review
        fields = ("id", "book", "rate", "description")
        read_only_fields = ("id", "book")
