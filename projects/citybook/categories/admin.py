from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

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
    
