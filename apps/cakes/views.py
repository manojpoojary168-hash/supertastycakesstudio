from django.shortcuts import get_object_or_404, render

from apps.cakes.models import Cake, Category


def cake_list(request):
    categories = Category.objects.filter(is_active=True)
    cakes = (
        Cake.objects.filter(is_active=True)
        .select_related("category")
        .order_by("display_order", "name")
    )
    return render(
        request,
        "cakes/list.html",
        {
            "categories": categories,
            "cakes": cakes,
            "active_category": None,
        },
    )


def cake_list_by_category(request, slug):
    categories = Category.objects.filter(is_active=True)
    active_category = get_object_or_404(Category, slug=slug, is_active=True)
    cakes = (
        Cake.objects.filter(category=active_category, is_active=True)
        .select_related("category")
        .order_by("display_order", "name")
    )
    return render(
        request,
        "cakes/list.html",
        {
            "categories": categories,
            "cakes": cakes,
            "active_category": active_category,
        },
    )


def cake_detail(request, slug):
    cake = get_object_or_404(
        Cake.objects.select_related("category"),
        slug=slug,
        is_active=True,
    )
    return render(request, "cakes/detail.html", {"cake": cake})


def menu(request):
    categories = Category.objects.filter(is_active=True).prefetch_related("cakes")
    menu_data = []
    for category in categories:
        cakes = [c for c in category.cakes.all() if c.is_active]
        if cakes:
            menu_data.append({"category": category, "cakes": cakes})

    return render(request, "cakes/menu.html", {"menu_data": menu_data})
