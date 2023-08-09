from django.contrib import admin

from .models import Book, Author, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("fullname", "birthdate", "total_books")
    search_fields = ("first_name", "last_name")
    date_hierarchy = "birthdate"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ["title", "author", "publish_year"]
    list_filter = ["author", "publish_year"]
    search_fields = ["title", "description", "author__first_name", "author__last_name"]
