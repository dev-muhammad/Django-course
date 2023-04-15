from django.contrib import admin
from django.contrib.auth.models import Group
from my_app.models import Book

admin.site.unregister(Group)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    model = Book
    list_display = ("id", "title", "author", "cover_type", "publish_year", "my_field")
    list_filter = ("publish_year", "cover_type")
    search_fields = ("title", "author")
    list_display_links = ("id", "title")
    list_per_page = 10
    date_hierarchy = "create_time"
    
    def my_field(self, instance):
        return f"Hello {instance.publish_year}"
    my_field.short_description = "Кастомное поле"

#admin.site.register(Book, BookAdmin)
