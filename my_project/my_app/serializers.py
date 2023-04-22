from rest_framework import serializers

from my_app.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class BookShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "author")
