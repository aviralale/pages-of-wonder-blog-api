from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_active')
    list_filter = ('is_admin','is_active')

    fieldsets = (
        (None, {
            "fields": (
                "email",
                "username",
                "password", 
            ),
        }),
        (
            "Personal Info",{
                "fields":(
                    "first_name",
                    "last_name",
                    "display_name"
                    ),
            }
        ),
        (
            "Permissions",{
                "fields":(
                    "is_active",
                    "is_staff",
                    "is_admin",
                    "groups",
                    "user_permissions",
                    ),
                    }
    ),
     ("Important dates", {"fields": ("date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "is_admin",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name", "username")
    ordering = ("username",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
    