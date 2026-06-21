"""Inject site-wide context into every template."""

from .models import ContactInformation, SiteSettings


def site_context(request):
    return {
        "site_settings": SiteSettings.load(),
        "contact": ContactInformation.load(),
    }
