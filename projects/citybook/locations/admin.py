from django.contrib import admin

from .models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = ["title", "description", "create_time", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["title", "description"]
    readonly_fields = ['create_time', 'update_time']
    date_hierarchy = "create_time"

@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ["title", "description", "country", "create_time", "is_active"]
    list_filter = ["country", "is_active"]
    search_fields = ["title", "description"]
    readonly_fields = ['create_time', 'update_time']
    date_hierarchy = "create_time"

