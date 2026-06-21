from django.db import models
from django.utils.text import slugify


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.PROTECT,
        related_name="images",
    )
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(
        default=False,
        help_text="Show on homepage Instagram preview section.",
    )
    display_order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-uploaded_at"]

    def __str__(self):
        return self.caption or f"Image #{self.pk}"
