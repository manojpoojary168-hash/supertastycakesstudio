from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomCakeRequestForm
from .models import CustomCakeRequest


def custom_cake_request(request):
    if request.method == "POST":
        form = CustomCakeRequestForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect(
                reverse("custom_orders:thank_you") + f"?id={instance.pk}"
            )
    else:
        form = CustomCakeRequestForm()

    return render(request, "custom_orders/request.html", {"form": form})


def thank_you(request):
    request_id = request.GET.get("id", "")
    custom_request = None
    if request_id:
        custom_request = CustomCakeRequest.objects.filter(pk=request_id).first()
    return render(
        request,
        "custom_orders/thank_you.html",
        {
            "request_id": request_id,
            "custom_request": custom_request,
        },
    )
