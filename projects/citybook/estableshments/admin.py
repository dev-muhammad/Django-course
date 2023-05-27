from django.contrib import admin

from .models import Place, GpsLocation, Contact, WorkingHours, Photo, CommonWorkingHours


class GpsLocationInline(admin.StackedInline):
    model = GpsLocation

class ContactInline(admin.StackedInline):
    model = Contact

class WorkingHoursInline(admin.TabularInline):
    model = WorkingHours
    verbose_name_plural = "Рабочее время (если отличается от стандартного)"
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = [ContactInline, GpsLocationInline, WorkingHoursInline, PhotoInline]

    list_display = ["title", "description", "create_time", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["title", "description"]
    readonly_fields = ['create_time', 'update_time']


@admin.register(CommonWorkingHours)
class CommonWorkingHoursAdmin(admin.ModelAdmin):

    list_display = ["day", "start_time", "end_time"]
