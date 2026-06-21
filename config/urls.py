"""
Root URL configuration for Super Tasty Cakes Studio.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.cakes import views as cake_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("cakes/", include("apps.cakes.urls")),
    path("menu/", cake_views.menu, name="menu"),
    path("gallery/", include("apps.gallery.urls")),
    path("custom-cake/", include("apps.custom_orders.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
