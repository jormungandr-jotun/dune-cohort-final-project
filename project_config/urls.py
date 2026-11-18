from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("listings.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("listings.api_urls")),
    path("api-token-auth/", include("project_config.api_urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
