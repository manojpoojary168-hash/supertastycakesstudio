from django.contrib import admin
from django.utils.html import format_html

from apps.core.admin_mixins import admin_image_preview

from .models import CustomCakeRequest

STATUS_COLORS = {
    CustomCakeRequest.Status.NEW: "#dc3545",
    CustomCakeRequest.Status.REVIEWED: "#fd7e14",
    CustomCakeRequest.Status.QUOTED: "#0d6efd",
    CustomCakeRequest.Status.CONFIRMED: "#6f42c1",
    CustomCakeRequest.Status.COMPLETED: "#198754",
    CustomCakeRequest.Status.CANCELLED: "#6c757d",
}


@admin.register(CustomCakeRequest)
class CustomCakeRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "phone_number",
        "occasion",
        "delivery_date",
        "status_badge",
        "quoted_price",
        "created_at",
    )
    list_filter = ("status", "occasion", "weight", "delivery_date", "created_at")
    search_fields = ("customer_name", "phone_number", "flavor", "design_description")
    readonly_fields = ("reference_image_preview", "created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    actions = (
        "mark_reviewed",
        "mark_confirmed",
        "mark_completed",
        "mark_cancelled",
    )

    fieldsets = (
        (
            "Customer",
            {
                "fields": ("customer_name", "phone_number"),
            },
        ),
        (
            "Cake Details",
            {
                "fields": (
                    "occasion",
                    "flavor",
                    "weight",
                    "delivery_date",
                    "design_description",
                    "reference_image",
                    "reference_image_preview",
                ),
            },
        ),
        (
            "Admin",
            {
                "fields": (
                    "status",
                    "quoted_price",
                    "admin_notes",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        color = STATUS_COLORS.get(obj.status, "#6c757d")
        return format_html(
            '<span style="background:{}; color:#fff; padding:3px 10px; '
            'border-radius:12px; font-size:12px; font-weight:600;">{}</span>',
            color,
            obj.get_status_display(),
        )

    @admin.display(description="Reference Preview")
    def reference_image_preview(self, obj):
        return admin_image_preview(obj.reference_image, max_height=200, max_width=300)

    @admin.action(description="Mark as reviewed")
    def mark_reviewed(self, request, queryset):
        queryset.update(status=CustomCakeRequest.Status.REVIEWED)

    @admin.action(description="Mark as confirmed")
    def mark_confirmed(self, request, queryset):
        queryset.update(status=CustomCakeRequest.Status.CONFIRMED)

    @admin.action(description="Mark as completed")
    def mark_completed(self, request, queryset):
        queryset.update(status=CustomCakeRequest.Status.COMPLETED)

    @admin.action(description="Mark as cancelled")
    def mark_cancelled(self, request, queryset):
        queryset.update(status=CustomCakeRequest.Status.CANCELLED)
