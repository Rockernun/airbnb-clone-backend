from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("avatar", "gender", "language", "currency", "username", "password", "name",
                "email", "is_host"),
            },
        ),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        },),
        ("Important Dates", {"fields": ("last_login",
        "date_joined"),
        },)
    )

    list_display = ("username", "email", "name", "is_host")