from django.urls import path

from . import views

app_name = "cakes"

urlpatterns = [
    path("", views.cake_list, name="list"),
    path("category/<slug:slug>/", views.cake_list_by_category, name="list_by_category"),
    path("<slug:slug>/", views.cake_detail, name="detail"),
]
