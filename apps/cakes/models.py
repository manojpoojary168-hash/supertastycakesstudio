from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Cake(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="cakes",
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.CharField(max_length=160, blank=True)
    description = models.TextField(blank=True)
    image = CloudinaryField("image", blank=True, null=True)
    price_half_kg = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    price_one_kg = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    price_per_piece = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    price_display_note = models.CharField(
        max_length=100,
        blank=True,
        help_text='Optional override, e.g. "₹35 / ₹70"',
    )
    has_egg_option = models.BooleanField(default=True)
    has_eggless_option = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def starting_price(self):
        """Lowest available price — shown on cake cards."""
        if self.price_display_note:
            return self.price_display_note
        prices = [
            p
            for p in (self.price_half_kg, self.price_one_kg, self.price_per_piece)
            if p is not None
        ]
        if prices:
            return min(prices)
        return None
