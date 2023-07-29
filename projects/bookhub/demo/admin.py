from django.contrib import admin

from .models import Book, Author, Category, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["author", "phone", "email"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "author_phone", "total_books"]
    search_fields = ["first_name", "last_name"]
    date_hierarchy = "birthdate"

    def author_phone(self, obj):
        return obj.contacts.phone
    author_phone.short_description = "Телефон"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ["name", "author", "publisher", "publish_year", "is_active"]
    list_filter = ["author", "publish_year", "is_active"]
    search_fields = ["name", "description", "author__first_name"]
    #readonly_fields = ['create_time', 'update_time']
    #date_hierarchy = "create_time"
