from .settings import *

# Don't test in debug mode
DEBUG = False

# Use in memory file storage
STORAGES["default"]["BACKEND"] = "django.core.files.storage.InMemoryStorage"

# Use a dummy cache
CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}

# Make whitenoise work a little faster
WHITENOISE_AUTOREFRESH = True

# Use a faster password hasher for testing
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Keep django-debug-toolbar out of testing
USE_DEBUG_TOOLBAR = False
if "debug_toolbar" in INSTALLED_APPS:
    INSTALLED_APPS.remove("debug_toolbar")
if "debug_toolbar.middleware.DebugToolbarMiddleware" in MIDDLEWARE:
    MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
