from django.contrib import admin

from apps.core.admin_mixins import SingletonAdmin, admin_image_preview

from .models import ContactInformation, Review, SiteSettings

admin.site.site_header = "Super Tasty Cakes Studio"
admin.site.site_title = "STC Admin"
admin.site.index_title = "Dashboard"


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    readonly_fields = ("hero_image_preview",)

    fieldsets = (
        (
            "Branding",
            {
                "fields": (
                    "site_name",
                    "business_tagline",
                    "owner_name",
                    "established_year",
                ),
            },
        ),
        (
            "Homepage Hero",
            {
                "fields": (
                    "hero_headline",
                    "hero_subheadline",
                    "hero_image",
                    "hero_image_preview",
                    "about_text",
                ),
            },
        ),
        (
            "Social & Maps",
            {
                "fields": (
                    "instagram_url",
                    "instagram_handle",
                    "google_maps_embed",
                ),
            },
        ),
    )

    @admin.display(description="Preview")
    def hero_image_preview(self, obj):
        return admin_image_preview(obj.hero_image, max_height=120, max_width=200)


@admin.register(ContactInformation)
class ContactInformationAdmin(SingletonAdmin):
    fieldsets = (
        (
            "Phone & WhatsApp",
            {
                "fields": ("phone_primary", "whatsapp_number", "email"),
            },
        ),
        (
            "Address",
            {
                "fields": ("business_address", "city", "state"),
            },
        ),
        (
            "Delivery & Hours",
            {
                "fields": ("delivery_areas", "business_hours"),
            },
        ),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "customer_location",
        "rating_display",
        "is_featured",
        "display_order",
        "created_at",
    )
    list_editable = ("is_featured", "display_order")
    list_filter = ("is_featured", "rating", "created_at")
    search_fields = ("customer_name", "customer_location", "review_text")
    ordering = ("display_order", "-created_at")
    date_hierarchy = "created_at"
    actions = ("mark_featured", "unmark_featured")

    @admin.display(description="Rating", ordering="rating")
    def rating_display(self, obj):
        return f"{obj.rating} ★"

    @admin.action(description="Mark as featured")
    def mark_featured(self, request, queryset):
        queryset.update(is_featured=True)

    @admin.action(description="Remove from featured")
    def unmark_featured(self, request, queryset):
        queryset.update(is_featured=False)
