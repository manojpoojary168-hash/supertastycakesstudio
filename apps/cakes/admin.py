from django.contrib import admin

from apps.core.admin_mixins import admin_image_preview

from .models import Cake, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "display_order", "is_active", "cake_count")
    list_editable = ("display_order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("display_order", "name")

    @admin.display(description="Cakes")
    def cake_count(self, obj):
        return obj.cakes.count()


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = (
        "image_thumb",
        "name",
        "category",
        "starting_price_display",
        "is_featured",
        "is_active",
        "display_order",
    )
    list_editable = (
        "is_featured",
        "is_active",
        "display_order",
    )
    list_filter = ("category", "is_featured", "is_active", "has_egg_option", "has_eggless_option")
    search_fields = ("name", "slug", "short_description", "description")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("image_preview", "created_at")
    ordering = ("display_order", "name")
    actions = ("mark_featured", "unmark_featured", "activate", "deactivate")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "category",
                    "name",
                    "slug",
                    "short_description",
                    "description",
                    "image",
                    "image_preview",
                ),
            },
        ),
        (
            "Pricing",
            {
                "fields": (
                    "price_half_kg",
                    "price_one_kg",
                    "price_per_piece",
                    "price_display_note",
                ),
            },
        ),
        (
            "Options & Visibility",
            {
                "fields": (
                    "has_egg_option",
                    "has_eggless_option",
                    "is_featured",
                    "is_active",
                    "display_order",
                    "created_at",
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

    @admin.display(description="From")
    def starting_price_display(self, obj):
        price = obj.starting_price
        if price is None:
            return "—"
        if isinstance(price, str):
            return price
        return f"₹{price}"

    @admin.action(description="Mark as featured")
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)

    @admin.action(description="Remove from featured")
    def unmark_featured(self, request, queryset):
        queryset.update(is_featured=False)

    @admin.action(description="Activate selected cakes")
    def activate(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Deactivate selected cakes")
    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
