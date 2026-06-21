"""WhatsApp message builders and URL helpers."""

from urllib.parse import quote

from django.conf import settings


def get_whatsapp_number(contact=None):
    if contact and contact.whatsapp_number:
        return contact.whatsapp_number.strip().lstrip("+")
    return settings.DEFAULT_WHATSAPP_NUMBER


def build_whatsapp_url(number, message):
    return f"https://wa.me/{number}?text={quote(message)}"


def generic_order_message():
    return (
        "Hello Super Tasty Cakes Studio,\n\n"
        "I'd like to place a cake order.\n"
        "Please share availability and details."
    )


def cake_order_message(cake, weight="1 kg", price=None, egg_type="Eggless"):
    name = getattr(cake, "name", str(cake))
    if price is None:
        price = getattr(cake, "price_one_kg", None) or getattr(cake, "starting_price", "—")
    if hasattr(price, "__float__"):
        price = f"₹{price}"
    return (
        "Hello Super Tasty Cakes Studio,\n\n"
        "I would like to order:\n\n"
        f"🎂 Cake: {name}\n"
        f"⚖️ Weight: {weight}\n"
        f"💰 Price: {price}\n"
        f"🥚 Type: {egg_type}\n\n"
        "Please let me know availability and delivery date.\n\n"
        "Thank you!"
    )


def custom_cake_message(request_id, occasion, delivery_date):
    return (
        "Hello Super Tasty Cakes Studio,\n\n"
        f"I just submitted a custom cake request (#{request_id}).\n\n"
        f"Occasion: {occasion}\n"
        f"Date needed: {delivery_date}\n\n"
        "Please confirm."
    )


def whatsapp_url(contact=None, message=None):
    number = get_whatsapp_number(contact)
    text = message or generic_order_message()
    return build_whatsapp_url(number, text)
