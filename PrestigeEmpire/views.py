from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteContent, Video


def home(request):
    content, _ = SiteContent.objects.get_or_create(pk=1)
    videos = Video.objects.filter(is_published=True)
    return render(request, "PrestigeEmpire/home.html", {"content": content, "videos": videos})


def robots(request):
    return HttpResponse("User-agent: *\\nAllow: /\\n", content_type="text/plain")


def sitemap(request):
    return HttpResponse("", content_type="application/xml")
