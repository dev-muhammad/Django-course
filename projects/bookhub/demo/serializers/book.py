from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # fields = ['pk', "name", "author", "categories", "publish_year", "publisher", "description", "pages", "is_active"]
        fields = "__all__"
