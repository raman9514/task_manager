from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "task_type", "status", "created_at", "completed_at")
    search_fields = ("name", "description", "task_type", "status")
    list_filter = ("task_type", "status", "created_at")
    ordering = ("-created_at",)

    fieldsets = (
        ("Task Details", {"fields": ("name", "description", "task_type", "status")}),
        ("Assignments", {"fields": ("assigned_users",)}),
        ("Timestamps", {"fields": ("created_at", "completed_at")}),
    )

    readonly_fields = ("created_at", "completed_at")

