"""Shared admin mixins and helpers."""

from django.contrib import admin
from django.utils.html import format_html


def admin_image_preview(image_field, max_height=80, max_width=120):
    if image_field:
        return format_html(
            '<img src="{}" style="max-height: {}px; max-width: {}px; '
            'border-radius: 4px; object-fit: cover;" />',
            image_field.url,
            max_height,
            max_width,
        )
    return "—"


class SingletonAdmin(admin.ModelAdmin):
    """Edit-only admin for singleton models — no add/delete."""

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
