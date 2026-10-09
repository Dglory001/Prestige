"""URL configuration for Prestige project."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from PrestigeEmpire import views

urlpatterns = [
    path("", views.home, name="home"),
    path("robots.txt", views.robots, name="robots"),
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("admin/", admin.site.urls),
    # Render does not serve MEDIA_URL itself.
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
