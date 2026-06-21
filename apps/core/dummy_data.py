"""Fallback content when the database has no records yet."""

from decimal import Decimal


DUMMY_CATEGORIES = [
    {"name": "Classic Cakes", "slug": "classic", "display_order": 1},
    {"name": "Premium Cakes", "slug": "premium", "display_order": 2},
    {"name": "Special Cakes", "slug": "special", "display_order": 3},
    {"name": "Treats", "slug": "treats", "display_order": 4},
]

DUMMY_CAKES = [
    {
        "name": "Chocolate Truffle",
        "slug": "chocolate-truffle",
        "category_slug": "classic",
        "category_name": "Classic Cakes",
        "short_description": "Rich dark chocolate layers with silky truffle ganache.",
        "description": "Our signature chocolate truffle cake — layers of moist chocolate sponge with decadent ganache. Available in egg and eggless.",
        "image_url": "https://placehold.co/400x500/FFF8F0/4A3728?text=Chocolate+Truffle&font=playfair-display",
        "price_half_kg": Decimal("450"),
        "price_one_kg": Decimal("850"),
        "price_per_piece": None,
        "starting_price": Decimal("450"),
        "has_egg_option": True,
        "has_eggless_option": True,
        "is_featured": True,
    },
    {
        "name": "Black Forest",
        "slug": "black-forest",
        "category_slug": "classic",
        "category_name": "Classic Cakes",
        "short_description": "Classic cherry and whipped cream delight.",
        "description": "A timeless favourite with chocolate sponge, fresh cream, and cherries.",
        "image_url": "https://placehold.co/400x500/EFE3D0/4A3728?text=Black+Forest&font=playfair-display",
        "price_half_kg": Decimal("400"),
        "price_one_kg": Decimal("750"),
        "price_per_piece": None,
        "starting_price": Decimal("400"),
        "has_egg_option": True,
        "has_eggless_option": True,
        "is_featured": True,
    },
    {
        "name": "Red Velvet",
        "slug": "red-velvet",
        "category_slug": "premium",
        "category_name": "Premium Cakes",
        "short_description": "Velvety crimson sponge with cream cheese frosting.",
        "description": "Premium red velvet with smooth cream cheese frosting — perfect for celebrations.",
        "image_url": "https://placehold.co/400x500/FFF8F0/C9A961?text=Red+Velvet&font=playfair-display",
        "price_half_kg": Decimal("500"),
        "price_one_kg": Decimal("950"),
        "price_per_piece": None,
        "starting_price": Decimal("500"),
        "has_egg_option": True,
        "has_eggless_option": True,
        "is_featured": True,
    },
    {
        "name": "Butterscotch Crunch",
        "slug": "butterscotch-crunch",
        "category_slug": "classic",
        "category_name": "Classic Cakes",
        "short_description": "Crunchy butterscotch with caramel drizzle.",
        "description": "Light sponge with butterscotch cream and crunchy praline topping.",
        "image_url": "https://placehold.co/400x500/EFE3D0/4A3728?text=Butterscotch&font=playfair-display",
        "price_half_kg": Decimal("420"),
        "price_one_kg": Decimal("800"),
        "price_per_piece": None,
        "starting_price": Decimal("420"),
        "has_egg_option": True,
        "has_eggless_option": True,
        "is_featured": True,
    },
    {
        "name": "Designer Wedding Cake",
        "slug": "designer-wedding",
        "category_slug": "special",
        "category_name": "Special Cakes",
        "short_description": "Custom multi-tier wedding centrepiece.",
        "description": "Elegant multi-tier wedding cakes designed to your theme. Consultation included.",
        "image_url": "https://placehold.co/400x500/FFF8F0/2D1F14?text=Wedding+Cake&font=playfair-display",
        "price_half_kg": None,
        "price_one_kg": Decimal("1200"),
        "price_per_piece": None,
        "starting_price": Decimal("1200"),
        "has_egg_option": True,
        "has_eggless_option": True,
        "is_featured": True,
    },
    {
        "name": "Cupcake Box (6 pcs)",
        "slug": "cupcake-box",
        "category_slug": "treats",
        "category_name": "Treats",
        "short_description": "Assorted flavours — perfect for gifting.",
        "description": "Box of 6 assorted cupcakes in flavours of your choice.",
        "image_url": "https://placehold.co/400x500/EFE3D0/C9A961?text=Cupcakes&font=playfair-display",
        "price_half_kg": None,
        "price_one_kg": None,
        "price_per_piece": Decimal("350"),
        "starting_price": Decimal("350"),
        "has_egg_option": True,
        "has_eggless_option": True,
        "is_featured": True,
    },
]

DUMMY_REVIEWS = [
    {
        "customer_name": "Priya S.",
        "customer_location": "Kundapur",
        "rating": 5,
        "review_text": "The chocolate truffle cake was absolutely divine! Fresh, moist, and delivered on time.",
    },
    {
        "customer_name": "Rajesh M.",
        "customer_location": "Byndoor",
        "rating": 5,
        "review_text": "Ordered a custom birthday cake for my daughter — she loved the design. Highly recommend!",
    },
    {
        "customer_name": "Anita K.",
        "customer_location": "Gangolli",
        "rating": 5,
        "review_text": "Best eggless cakes in the area. Smita understood exactly what we wanted.",
    },
    {
        "customer_name": "Suresh P.",
        "customer_location": "Kundapur",
        "rating": 4,
        "review_text": "Great taste and beautiful presentation. Will order again for our anniversary.",
    },
]

DUMMY_GALLERY = [
    {"caption": "Engagement Cake", "category_slug": "engagement", "category_name": "Engagement",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Engagement"},
    {"caption": "Birthday Theme", "category_slug": "birthday", "category_name": "Birthday",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Birthday"},
    {"caption": "Wedding Tier", "category_slug": "wedding", "category_name": "Wedding",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Wedding"},
    {"caption": "Princess Theme", "category_slug": "girls-theme", "category_name": "Girls Theme",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Girls+Theme"},
    {"caption": "Superhero Theme", "category_slug": "boys-theme", "category_name": "Boys Theme",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Boys+Theme"},
    {"caption": "Custom Designer", "category_slug": "custom-designer", "category_name": "Custom Designer",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Custom"},
    {"caption": "Anniversary Cake", "category_slug": "birthday", "category_name": "Birthday",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Anniversary"},
    {"caption": "Floral Wedding", "category_slug": "wedding", "category_name": "Wedding",
     "image_url": "https://placehold.co/400x400/E8DCC4/4A3728?text=Floral"},
]

DUMMY_GALLERY_CATEGORIES = [
    {"name": "Engagement", "slug": "engagement"},
    {"name": "Birthday", "slug": "birthday"},
    {"name": "Wedding", "slug": "wedding"},
    {"name": "Girls Theme", "slug": "girls-theme"},
    {"name": "Boys Theme", "slug": "boys-theme"},
    {"name": "Custom Designer", "slug": "custom-designer"},
]

DUMMY_USPS = [
    {"title": "Freshly Baked", "description": "Every cake is baked fresh to order — never frozen or pre-made.", "icon": "bi-fire"},
    {"title": "Egg & Eggless", "description": "Full range available in both egg and eggless options.", "icon": "bi-heart"},
    {"title": "Custom Designs", "description": "From simple birthdays to elaborate wedding tiers — we design it all.", "icon": "bi-brush"},
    {"title": "Local Delivery", "description": "Delivery across Byndoor, Gangolli, Kundapur and nearby areas.", "icon": "bi-truck"},
]

DEFAULT_DELIVERY_AREAS = ["Byndoor", "Gangolli", "Kundapur", "Nearby Areas"]
