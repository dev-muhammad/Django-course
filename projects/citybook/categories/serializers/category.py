from rest_framework.serializers import ModelSerializer

from ..models import Category


class CategoryShortSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title"]


class CategoryFullSerializer(ModelSerializer):

    parent = CategoryShortSerializer()

    class Meta:
        model = Category
        fields = ["id", "title", "description", "parent"]


class CategoryChildsSerializer(ModelSerializer):

    subcategories = CategoryShortSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "description", "subcategories"]


class CategoryCreateSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "description", "parent"]
