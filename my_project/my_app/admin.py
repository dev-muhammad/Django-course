from django.contrib import admin
from django.contrib.auth.models import Group
from my_app.models import Book, Author, Category, Contact

admin.site.unregister(Group)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ("fullname", "book_counts")

    def book_counts(self, instance):
        return instance.books.count()
    book_counts.short_description = "Количество книг"
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "author", "cover_type", "publish_year", "my_categories", "my_field")
    list_filter = ("publish_year", "cover_type")
    search_fields = ("title", "author")
    list_display_links = ("id", "title")
    list_per_page = 10
    date_hierarchy = "create_time"
    
    def my_categories(self, instance):
        return ", ".join([i[0] for i in instance.categories.all().values_list("title")])
        # return ", ".join([i.title for i in instance.categories.all()])
    my_categories.short_description = "Категории"

    def my_field(self, instance):
        return f"Hello {instance.publish_year}"
    my_field.short_description = "Кастомное поле"

#admin.site.register(Book, BookAdmin)
