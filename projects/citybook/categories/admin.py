from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import Category


class CategoryInline(admin.TabularInline):
    model = Category
    fk_name = "parent"
    fields = ["title", "description", "is_active"]
    extra = 0
    verbose_name_plural = "Подкатегории"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    inlines = [CategoryInline,]
               
    list_display = ["title", "description", "parent", "create_time", "is_active"]
    list_filter = ["parent", "is_active"]
    search_fields = ["title", "description"]
    readonly_fields = ['create_time', 'update_time']
    date_hierarchy = "create_time"

    add_fieldsets = (
        (None, {'fields': ('title', 'description', 'parent')}),
    )
    
    change_fieldsets = (
        ('Основной', {
            'fields': ('title', 'description', 'parent',)
        }),
        ('Активность', {
            'fields': ('is_active',)
        }),
        ('Дата и время', {
            'fields': ('create_time', "update_time"),
        })
    )
    
    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.change_fieldsets
        else:
            return  self.add_fieldsets
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).select_related("parent").prefetch_related("subcategories")
    
