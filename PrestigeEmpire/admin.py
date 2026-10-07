from django.contrib import admin
from .models import SiteContent, Video


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "city", "contact_email", "whatsapp_number")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title",)
