from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import your custom User model

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "mobile", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "email", "mobile")
    list_filter = ("is_active", "is_staff", "is_superuser")
    ordering = ("-date_joined",)

    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "mobile", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            "Create User",
            {
                "classes": ("wide",),
                "fields": ("username", "email", "mobile", "password1", "password2"),
            },
        ),
    )

