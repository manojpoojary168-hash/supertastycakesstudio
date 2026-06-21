from django.shortcuts import render

from apps.cakes.models import Cake
from apps.core.dummy_data import DUMMY_USPS
from apps.core.models import ContactInformation, Review
from apps.gallery.models import GalleryImage


def home(request):
    featured_cakes = list(
        Cake.objects.filter(is_featured=True, is_active=True).select_related("category")[:6]
    )
    reviews = list(
        Review.objects.filter(is_featured=True).order_by("display_order", "-created_at")[:6]
    )
    gallery_images = list(
        GalleryImage.objects.filter(is_featured=True)
        .select_related("category")
        .order_by("display_order", "-uploaded_at")[:8]
    )
    contact = ContactInformation.load()
    areas = contact.delivery_areas_list

    return render(
        request,
        "core/home.html",
        {
            "featured_cakes": featured_cakes,
            "reviews": reviews,
            "gallery_images": gallery_images,
            "usps": DUMMY_USPS,
            "delivery_areas": areas,
        },
    )


def contact(request):
    return render(request, "core/contact.html")
