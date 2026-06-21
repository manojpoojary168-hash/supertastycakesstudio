"""
Production settings for Render deployment — Postgres + Cloudinary + security headers.
"""
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F401, F403

DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS")  # noqa: F405

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

# Cloudinary for all uploaded media in production
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Require Cloudinary credentials in production (admin image uploads)
for _cloudinary_key in ("CLOUD_NAME", "API_KEY", "API_SECRET"):
    if not CLOUDINARY_STORAGE.get(_cloudinary_key):  # noqa: F405
        raise ImproperlyConfigured(
            f"CLOUDINARY_{_cloudinary_key} must be set in production for media uploads."
        )

# CSRF — required for HTTPS form POSTs on Render (custom cake request, admin login)
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS")  # noqa: F405

# Security
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env("DJANGO_LOG_LEVEL", default="INFO"),  # noqa: F405
            "propagate": False,
        },
    },
}
