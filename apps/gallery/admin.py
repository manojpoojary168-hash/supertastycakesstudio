from django.contrib import admin

from apps.core.admin_mixins import admin_image_preview

from .models import GalleryCategory, GalleryImage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "display_order", "is_active", "image_count")
    list_editable = ("display_order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("display_order", "name")

    @admin.display(description="Images")
    def image_count(self, obj):
        return obj.images.count()


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = (
        "image_thumb",
        "caption",
        "category",
        "is_featured",
        "display_order",
        "uploaded_at",
    )
    list_editable = ("is_featured", "display_order")
    list_filter = ("category", "is_featured", "uploaded_at")
    search_fields = ("caption", "category__name")
    readonly_fields = ("image_preview", "uploaded_at")
    ordering = ("display_order", "-uploaded_at")
    actions = ("mark_featured", "unmark_featured")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "category",
                    "image",
                    "image_preview",
                    "caption",
                    "is_featured",
                    "display_order",
                    "uploaded_at",
                ),
            },
        ),
    )

    @admin.display(description="Image")
    def image_thumb(self, obj):
        return admin_image_preview(obj.image, max_height=50, max_width=50)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return admin_image_preview(obj.image, max_height=200, max_width=300)

    @admin.action(description="Mark as featured")
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)

    @admin.action(description="Remove from featured")
    def unmark_featured(self, request, queryset):
        queryset.update(is_featured=False)
