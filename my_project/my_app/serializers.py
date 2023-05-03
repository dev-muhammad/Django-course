from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from my_app.models import Book, Author, Category, Contact

class Test(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10, min_length=5)



class ContactSerializer(serializers.ModelSerializer):
    
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ("phone", "email", "custom_field")

    def get_custom_field(self, instance):
        return instance.author.first_name

    def to_representation(self, instance, *args, **kwargs):
        data = super(ContactSerializer, self).to_representation(instance)
        data["test"] = "test value"
        return data

class CategoryFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
    
    def to_representation(self, instance, *args, **kwargs):
        data = super(CategorySerializer, self).to_representation(instance)
        return data["title"]

class AuthorSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="contacts.email")
    phone = serializers.CharField(source="contacts.phone")

    contacts = ContactSerializer()
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "email", "phone", "contacts")

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "author")


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    # def validate(self, data):
    #     value = data.get("publish_year")
    #     if value is None:
    #         raise serializers.ValidationError({"publish_year":"Поле publish_year объязательный"})
    #     if int(value) > 2023:
    #         raise serializers.ValidationError({"publish_year":"Не ужеле это книга из будещего?"})
    #     return super().validate(data)

    def validate_publish_year(self, value):
        if int(value) > 2022:
            raise serializers.ValidationError("Не ужеле это книга из будещего?")
        
        return value

    def create(self, validated_data):
        validated_data["cover_type"] = "Hard cover"
        if validated_data.get("publish_year", True):
            validated_data["publish_year"]= "2023"
        return super().create(validated_data)
