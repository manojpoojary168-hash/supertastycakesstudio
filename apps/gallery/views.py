from django.shortcuts import render

from apps.gallery.models import GalleryCategory, GalleryImage


def gallery(request):
    category_slug = request.GET.get("category", "")
    categories = GalleryCategory.objects.filter(is_active=True)
    qs = GalleryImage.objects.select_related("category").order_by("display_order", "-uploaded_at")
    if category_slug:
        qs = qs.filter(category__slug=category_slug, category__is_active=True)

    return render(
        request,
        "gallery/gallery.html",
        {
            "categories": categories,
            "images": qs,
            "active_category": category_slug,
        },
    )
