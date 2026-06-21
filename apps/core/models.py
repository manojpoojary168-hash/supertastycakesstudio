from django.db import models

from .mixins import SingletonModelMixin


class SiteSettings(SingletonModelMixin, models.Model):
    site_name = models.CharField(max_length=100, default="Super Tasty Cakes Studio")
    hero_headline = models.CharField(max_length=200, default="Handcrafted Cakes for Every Celebration")
    hero_subheadline = models.TextField(
        blank=True,
        default="Fresh, beautiful cakes delivered across Byndoor, Gangolli, Kundapur & nearby areas.",
    )
    business_tagline = models.CharField(max_length=200, blank=True)
    hero_image = models.ImageField(upload_to="site/", blank=True, null=True)
    about_text = models.TextField(blank=True)
    established_year = models.PositiveIntegerField(default=2021)
    owner_name = models.CharField(max_length=100, blank=True)
    instagram_url = models.URLField(blank=True)
    instagram_handle = models.CharField(max_length=100, blank=True)
    google_maps_embed = models.TextField(
        blank=True,
        help_text="Paste the full Google Maps iframe embed code.",
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class ContactInformation(SingletonModelMixin, models.Model):
    phone_primary = models.CharField(max_length=20, default="+919075075993")
    whatsapp_number = models.CharField(
        max_length=20,
        default="919075075993",
        help_text="Digits only, no + prefix (used for wa.me links).",
    )
    email = models.EmailField(blank=True)
    business_address = models.TextField(blank=True)
    city = models.CharField(max_length=100, default="Byndoor")
    state = models.CharField(max_length=100, default="Karnataka")
    delivery_areas = models.TextField(
        blank=True,
        help_text="One delivery area per line (e.g. Byndoor, Gangolli, Kundapur).",
    )
    business_hours = models.TextField(
        blank=True,
        help_text="One line per entry, e.g. Mon–Sat: 9 AM – 7 PM",
    )

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"Contact — {self.city}"

    @property
    def delivery_areas_list(self):
        return [area.strip() for area in self.delivery_areas.splitlines() if area.strip()]


class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_location = models.CharField(max_length=100, blank=True)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} ★") for i in range(1, 6)]
    )
    review_text = models.TextField()
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Customer Review"

    def __str__(self):
        return f"{self.customer_name} — {self.rating}★"
