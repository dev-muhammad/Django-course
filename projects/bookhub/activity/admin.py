from django.contrib import admin

from .models import Favorite, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "rate", "create_time")
    search_fields = ("user__first_name", "user__last_name", "book__title", "description",)
    list_filter = ("rate",)
    date_hierarchy = "create_time"

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "status")
    search_fields = ("user__first_name", "user__last_name", "book__title", "description",)
    list_filter = ("status",)
    date_hierarchy = "create_time"
