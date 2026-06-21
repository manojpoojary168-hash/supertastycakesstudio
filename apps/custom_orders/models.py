from django.db import models


class CustomCakeRequest(models.Model):
    class Occasion(models.TextChoices):
        BIRTHDAY = "birthday", "Birthday"
        ANNIVERSARY = "anniversary", "Anniversary"
        WEDDING = "wedding", "Wedding"
        ENGAGEMENT = "engagement", "Engagement"
        OTHER = "other", "Other"

    class Weight(models.TextChoices):
        HALF_KG = "0.5kg", "0.5 kg"
        ONE_KG = "1kg", "1 kg"
        ONE_HALF_KG = "1.5kg", "1.5 kg"
        TWO_KG = "2kg", "2 kg"
        CUSTOM = "custom", "Custom"

    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEWED = "reviewed", "Reviewed"
        QUOTED = "quoted", "Quoted"
        CONFIRMED = "confirmed", "Confirmed"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    occasion = models.CharField(max_length=20, choices=Occasion.choices)
    flavor = models.CharField(max_length=100)
    weight = models.CharField(max_length=20, choices=Weight.choices)
    delivery_date = models.DateField()
    design_description = models.TextField()
    reference_image = models.ImageField(upload_to="custom_orders/", blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    admin_notes = models.TextField(blank=True, help_text="Private notes — not shown to customers.")
    quoted_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Custom Cake Request"

    def __str__(self):
        return f"#{self.pk} — {self.customer_name} ({self.get_status_display()})"
