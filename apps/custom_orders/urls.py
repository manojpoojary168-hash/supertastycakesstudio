from django.urls import path

from . import views

app_name = "custom_orders"

urlpatterns = [
    path("", views.custom_cake_request, name="request"),
    path("thank-you/", views.thank_you, name="thank_you"),
]
