from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models.user import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
