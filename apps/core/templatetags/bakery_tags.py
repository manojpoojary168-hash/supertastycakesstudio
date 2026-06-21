"""Template helpers for images and placeholders."""

from urllib.parse import quote

from django import template

register = template.Library()

PLACEHOLDER_BASE = "https://placehold.co/{w}x{h}/FFF8F0/4A3728"


def _placeholder_url(label, width=400, height=500):
    text = quote(label.replace(" ", "+"))
    return f"{PLACEHOLDER_BASE.format(w=width, h=height)}?text={text}&font=playfair-display"


@register.simple_tag
def placeholder_image(label, width=400, height=500):
    return _placeholder_url(label, width, height)


@register.simple_tag
def cake_image(cake, width=400, height=500):
    if cake.image:
        return cake.image.url
    return _placeholder_url(cake.name, width, height)


@register.simple_tag
def gallery_image(image_obj, width=400, height=400):
    if image_obj.image:
        return image_obj.image.url
    label = image_obj.caption or image_obj.category.name
    return _placeholder_url(label, width, height)
