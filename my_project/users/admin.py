from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class AdminUser(UserAdmin):
    
    list_display = ("id", "nickname", "phone", "email")
    list_filter = ("is_superuser", "is_active")
    filter_horizontal = ()
    ordering = ()
    search_fields = ["name", "bio"]

    add_fieldsets = (
        (None, {'fields': ('nickname', 'password1', "password2")}),
    )
    
    change_fieldsets = (
        ('Основной', {
            'fields': ('nickname', 'phone', 'email', 'password')
        }),
        ('Info', {
            'fields': ('gender', 'bio')
        }),
        ('Активность', {
            'fields': ('is_superuser', "is_staff", "is_active"),
        })
    )

    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.change_fieldsets
        else:
            return  self.add_fieldsets