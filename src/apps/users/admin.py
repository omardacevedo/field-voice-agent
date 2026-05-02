from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Technician


@admin.register(Technician)
class TechnicianAdmin(UserAdmin):
    list_display = ["email", "employee_id", "specialty", "is_active", "created_at"]
    list_filter = ["specialty", "is_active", "is_staff"]
    search_fields = ["email", "employee_id", "first_name", "last_name"]
    ordering = ["email"]
    readonly_fields = ["id", "created_at", "updated_at", "last_login"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "employee_id", "specialty", "phone")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Auditoría", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "employee_id", "password1", "password2"),
        }),
    )
