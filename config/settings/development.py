"""
Local development settings — SQLite database and filesystem media storage.
"""
from .base import *  # noqa: F401, F403

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

# Local filesystem for uploaded images during development
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_ROOT = BASE_DIR / "media"  # noqa: F405

# Email goes to console in development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
