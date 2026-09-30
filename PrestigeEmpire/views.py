from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'PrestigeEmpire/home.html')


def robots(request):
    return HttpResponse('User-agent: *\nAllow: /\nSitemap: https://prestigechampagne.cd/sitemap.xml\n', content_type='text/plain')


def sitemap(request):
    return HttpResponse(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        '<url><loc>https://prestigechampagne.cd/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>'
        '</urlset>',
        content_type='application/xml',
    )
