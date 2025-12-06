from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ("email", "name", "is_staff", "is_active", "is_verified", "created_at")
    list_filter = ("is_staff", "is_active", "is_verified")
    readonly_fields = ("created_at", "updated_at", "last_login")
    ordering = ("email",)
    search_fields = ("email", "name")
    fieldsets = (
        (None, {"fields": ("email", "password", "name")}),
        ("Estado", {"fields": ("is_active", "is_staff", "is_superuser", "is_verified")}),
        ("Seguridad", {"fields": ("mfa_secret",)}),
        ("Permisos", {"fields": ("groups", "user_permissions")}),
        ("Tiempos", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "name", "is_staff", "is_superuser"),
            },
        ),
    )
