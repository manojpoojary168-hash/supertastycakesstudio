"""
Load Super Tasty Cakes Studio sample catalogue and site content.

Usage:
    python manage.py load_sample_data
    python manage.py load_sample_data --flush
"""

from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.cakes.models import Cake, Category
from apps.core.models import ContactInformation, Review, SiteSettings
from apps.gallery.models import GalleryCategory, GalleryImage


SAMPLE_CATEGORIES = [
    ("Classic Cakes", "classic", 1),
    ("Premium Cakes", "premium", 2),
    ("Special Cakes", "special", 3),
    ("Treats", "treats", 4),
]

SAMPLE_CAKES = [
    {
        "name": "Chocolate Truffle",
        "category": "classic",
        "short_description": "Rich dark chocolate layers with silky truffle ganache.",
        "description": "Our signature chocolate truffle cake — layers of moist chocolate sponge with decadent ganache. Available in egg and eggless.",
        "price_half_kg": Decimal("450"),
        "price_one_kg": Decimal("850"),
        "is_featured": True,
        "display_order": 1,
    },
    {
        "name": "Black Forest",
        "category": "classic",
        "short_description": "Classic cherry and whipped cream delight.",
        "description": "A timeless favourite with chocolate sponge, fresh cream, and cherries.",
        "price_half_kg": Decimal("400"),
        "price_one_kg": Decimal("750"),
        "is_featured": True,
        "display_order": 2,
    },
    {
        "name": "Butterscotch Crunch",
        "category": "classic",
        "short_description": "Crunchy butterscotch with caramel drizzle.",
        "description": "Light sponge with butterscotch cream and crunchy praline topping.",
        "price_half_kg": Decimal("420"),
        "price_one_kg": Decimal("800"),
        "is_featured": True,
        "display_order": 3,
    },
    {
        "name": "Pineapple Gateau",
        "category": "classic",
        "short_description": "Light pineapple sponge with fresh cream.",
        "description": "Refreshing pineapple cake perfect for summer celebrations.",
        "price_half_kg": Decimal("380"),
        "price_one_kg": Decimal("720"),
        "is_featured": False,
        "display_order": 4,
    },
    {
        "name": "Red Velvet",
        "category": "premium",
        "short_description": "Velvety crimson sponge with cream cheese frosting.",
        "description": "Premium red velvet with smooth cream cheese frosting — perfect for celebrations.",
        "price_half_kg": Decimal("500"),
        "price_one_kg": Decimal("950"),
        "is_featured": True,
        "display_order": 5,
    },
    {
        "name": "Belgian Chocolate",
        "category": "premium",
        "short_description": "Intense Belgian chocolate with gold-dusted finish.",
        "description": "Luxurious Belgian chocolate cake for the true chocolate lover.",
        "price_half_kg": Decimal("550"),
        "price_one_kg": Decimal("1050"),
        "is_featured": True,
        "display_order": 6,
    },
    {
        "name": "Designer Wedding Cake",
        "category": "special",
        "short_description": "Custom multi-tier wedding centrepiece.",
        "description": "Elegant multi-tier wedding cakes designed to your theme. Consultation included.",
        "price_one_kg": Decimal("1200"),
        "price_display_note": "From ₹1200/kg — custom quote",
        "is_featured": True,
        "display_order": 7,
    },
    {
        "name": "Engagement Theme Cake",
        "category": "special",
        "short_description": "Romantic floral design for your special day.",
        "description": "Beautiful engagement cakes with custom toppers and floral accents.",
        "price_one_kg": Decimal("1100"),
        "is_featured": False,
        "display_order": 8,
    },
    {
        "name": "Birthday Photo Cake",
        "category": "special",
        "short_description": "Personalised edible photo print on cake.",
        "description": "Upload your photo — we'll print it on a delicious birthday cake.",
        "price_half_kg": Decimal("480"),
        "price_one_kg": Decimal("900"),
        "is_featured": False,
        "display_order": 9,
    },
    {
        "name": "Cupcake Box (6 pcs)",
        "category": "treats",
        "short_description": "Assorted flavours — perfect for gifting.",
        "description": "Box of 6 assorted cupcakes in flavours of your choice.",
        "price_per_piece": Decimal("350"),
        "price_display_note": "₹350 / box of 6",
        "is_featured": True,
        "display_order": 10,
    },
    {
        "name": "Chocolate Brownie",
        "category": "treats",
        "short_description": "Fudgy chocolate brownie — single serve.",
        "description": "Rich, fudgy brownie topped with chocolate ganache.",
        "price_per_piece": Decimal("70"),
        "price_display_note": "₹70 each",
        "is_featured": False,
        "display_order": 11,
    },
    {
        "name": "Mini Pastry Box",
        "category": "treats",
        "short_description": "Assorted mini pastries — 12 pieces.",
        "description": "A delightful box of 12 mini pastries in assorted flavours.",
        "price_per_piece": Decimal("450"),
        "price_display_note": "₹450 / box",
        "is_featured": False,
        "display_order": 12,
    },
]

SAMPLE_REVIEWS = [
    ("Priya S.", "Kundapur", 5, "The chocolate truffle cake was absolutely divine! Fresh, moist, and delivered on time.", 1),
    ("Rajesh M.", "Byndoor", 5, "Ordered a custom birthday cake for my daughter — she loved the design. Highly recommend!", 2),
    ("Anita K.", "Gangolli", 5, "Best eggless cakes in the area. Smita understood exactly what we wanted.", 3),
    ("Suresh P.", "Kundapur", 4, "Great taste and beautiful presentation. Will order again for our anniversary.", 4),
]

SAMPLE_GALLERY_CATEGORIES = [
    ("Engagement", "engagement", 1),
    ("Birthday", "birthday", 2),
    ("Wedding", "wedding", 3),
    ("Girls Theme", "girls-theme", 4),
    ("Boys Theme", "boys-theme", 5),
    ("Custom Designer", "custom-designer", 6),
]

SAMPLE_GALLERY_IMAGES = [
    ("engagement", "Engagement Floral Cake", True, 1),
    ("birthday", "Princess Birthday Theme", True, 2),
    ("wedding", "Three-Tier Wedding Cake", True, 3),
    ("girls-theme", "Unicorn Theme Cake", True, 4),
    ("boys-theme", "Superhero Theme Cake", True, 5),
    ("custom-designer", "Designer Anniversary Cake", True, 6),
    ("birthday", "Mickey Mouse Birthday", False, 7),
    ("wedding", "Floral Wedding Centrepiece", True, 8),
]


class Command(BaseCommand):
    help = "Load sample categories, cakes, reviews, gallery, and site configuration."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing catalogue data before loading (keeps singletons).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["flush"]:
            self.stdout.write("Flushing existing catalogue data…")
            Cake.objects.all().delete()
            Category.objects.all().delete()
            Review.objects.all().delete()
            GalleryImage.objects.all().delete()
            GalleryCategory.objects.all().delete()

        categories = {}
        for name, slug, order in SAMPLE_CATEGORIES:
            cat, _ = Category.objects.update_or_create(
                slug=slug,
                defaults={"name": name, "display_order": order, "is_active": True},
            )
            categories[slug] = cat
        self.stdout.write(self.style.SUCCESS(f"  {len(categories)} categories"))

        for item in SAMPLE_CAKES:
            data = item.copy()
            cat_slug = data.pop("category")
            Cake.objects.update_or_create(
                name=data["name"],
                defaults={
                    **data,
                    "category": categories[cat_slug],
                    "is_active": True,
                    "has_egg_option": True,
                    "has_eggless_option": True,
                },
            )
        self.stdout.write(self.style.SUCCESS(f"  {len(SAMPLE_CAKES)} cakes"))

        for name, location, rating, text, order in SAMPLE_REVIEWS:
            Review.objects.update_or_create(
                customer_name=name,
                customer_location=location,
                defaults={
                    "rating": rating,
                    "review_text": text,
                    "is_featured": True,
                    "display_order": order,
                },
            )
        self.stdout.write(self.style.SUCCESS(f"  {len(SAMPLE_REVIEWS)} reviews"))

        gallery_cats = {}
        for name, slug, order in SAMPLE_GALLERY_CATEGORIES:
            gc, _ = GalleryCategory.objects.update_or_create(
                slug=slug,
                defaults={"name": name, "display_order": order, "is_active": True},
            )
            gallery_cats[slug] = gc

        for cat_slug, caption, featured, order in SAMPLE_GALLERY_IMAGES:
            GalleryImage.objects.update_or_create(
                category=gallery_cats[cat_slug],
                caption=caption,
                defaults={"is_featured": featured, "display_order": order},
            )
        self.stdout.write(self.style.SUCCESS(f"  {len(SAMPLE_GALLERY_IMAGES)} gallery images"))

        contact = ContactInformation.load()
        contact.phone_primary = "+919075075993"
        contact.whatsapp_number = "919075075993"
        contact.email = "hello@supertastycakes.com"
        contact.business_address = "Main Road, Near Bus Stand"
        contact.city = "Byndoor"
        contact.state = "Karnataka"
        contact.delivery_areas = "Byndoor\nGangolli\nKundapur\nBhandiwada\nKollur\nNearby Areas"
        contact.business_hours = "Mon – Sat: 9 AM – 7 PM\nSunday: By appointment only"
        contact.save()
        self.stdout.write(self.style.SUCCESS("  Contact information updated"))

        settings = SiteSettings.load()
        settings.site_name = "Super Tasty Cakes Studio"
        settings.business_tagline = "Byndoor's Favourite Bakery"
        settings.hero_headline = "Handcrafted Cakes for Every Celebration"
        settings.hero_subheadline = (
            "Fresh, beautiful cakes delivered across Byndoor, Gangolli, Kundapur & nearby areas."
        )
        settings.about_text = (
            "Super Tasty Cakes Studio has been delighting families across coastal Karnataka "
            "since 2021 with freshly baked, beautifully designed cakes for every occasion."
        )
        settings.owner_name = "Smita"
        settings.established_year = 2021
        settings.instagram_url = "https://instagram.com/supertastycakes"
        settings.instagram_handle = "supertastycakes"
        settings.save()
        self.stdout.write(self.style.SUCCESS("  Site settings updated"))

        self.stdout.write(self.style.SUCCESS("\nSample data loaded successfully."))
