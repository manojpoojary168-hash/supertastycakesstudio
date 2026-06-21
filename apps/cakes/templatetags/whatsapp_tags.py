from django import template
from django.utils.html import format_html

from apps.cakes.utils import (
    cake_order_message,
    custom_cake_message,
    generic_order_message,
    get_whatsapp_number,
    whatsapp_url,
)

register = template.Library()


@register.simple_tag(takes_context=True)
def whatsapp_url_tag(context, message_type="generic", cake=None, **kwargs):
    contact = context.get("contact")
    if message_type == "cake" and cake:
        message = cake_order_message(
            cake,
            weight=kwargs.get("weight", "1 kg"),
            price=kwargs.get("price"),
            egg_type=kwargs.get("egg_type", "Eggless"),
        )
    elif message_type == "custom":
        message = custom_cake_message(
            kwargs.get("request_id", ""),
            kwargs.get("occasion", ""),
            kwargs.get("delivery_date", ""),
        )
    else:
        message = generic_order_message()
    return whatsapp_url(contact, message)


@register.simple_tag(takes_context=True)
def whatsapp_link(context, message_type="generic", cake=None, label="Order on WhatsApp", css_class="btn btn-whatsapp", **kwargs):
    url = whatsapp_url_tag(context, message_type, cake, **kwargs)
    return format_html(
        '<a href="{}" target="_blank" rel="noopener noreferrer" class="{}">'
        '<i class="bi bi-whatsapp me-2"></i>{}</a>',
        url,
        css_class,
        label,
    )


@register.simple_tag(takes_context=True)
def whatsapp_float_url(context):
    return whatsapp_url(context.get("contact"))
