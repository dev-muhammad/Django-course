from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ["name", "author", "publisher", "publish_year", "is_active"]
    list_filter = ["author", "publish_year", "is_active"]
    search_fields = ["name", "description", "author"]
    #readonly_fields = ['create_time', 'update_time']
    #date_hierarchy = "create_time"
