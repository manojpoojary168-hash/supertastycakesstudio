from django import forms

from crispy_forms.helper import FormHelper

from .models import CustomCakeRequest


class CustomCakeRequestForm(forms.ModelForm):
    class Meta:
        model = CustomCakeRequest
        fields = [
            "customer_name",
            "phone_number",
            "occasion",
            "flavor",
            "weight",
            "delivery_date",
            "design_description",
            "reference_image",
        ]
        widgets = {
            "customer_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "+91 98765 43210"}),
            "flavor": forms.TextInput(attrs={"placeholder": "e.g. Chocolate, Butterscotch, Red Velvet"}),
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "design_description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Describe your dream cake — theme, colours, message on cake…"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
