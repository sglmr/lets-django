from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #
    # Django admin
    path("admin/", admin.site.urls),
    # django-allauth
    path("accounts/", include("allauth.urls")),
    # django-browser-reload
    path("__reload__/", include("django_browser_reload.urls")),
]

# Serve static & media files with DEBUG turned on
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include debug toolbar when in use
if settings.USE_DEBUG_TOOLBAR is True:
    urlpatterns += debug_toolbar_urls()
