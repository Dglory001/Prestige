import os
from collections import deque
from io import BytesIO

from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


class SiteContent(models.Model):
    brand_name = models.CharField(max_length=100, default="Prestige Champagne")
    city = models.CharField(max_length=100, default="Kinshasa")
    coffret_image = models.ImageField(upload_to="coffrets/", blank=True, null=True)
    contact_email = models.EmailField(blank=True)
    whatsapp_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.brand_name

    def save(self, *args, **kwargs):
        should_detour = self.coffret_image and not self.coffret_image.name.startswith("coffrets/detoure_")
        super().save(*args, **kwargs)
        if should_detour:
            self._remove_white_background()

    def _remove_white_background(self):
        image = Image.open(self.coffret_image.path).convert("RGBA")
        pixels = image.load()
        width, height = image.size
        queue, visited = deque(), set()

        def is_white(x, y):
            r, g, b, _ = pixels[x, y]
            return r > 220 and g > 220 and b > 220

        for x in range(width):
            queue.extend(((x, 0), (x, height - 1)))
        for y in range(height):
            queue.extend(((0, y), (width - 1, y)))

        while queue:
            x, y = queue.popleft()
            if (x, y) in visited or not (0 <= x < width and 0 <= y < height) or not is_white(x, y):
                continue
            visited.add((x, y))
            r, g, b, _ = pixels[x, y]
            pixels[x, y] = (r, g, b, 0)
            queue.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

        output = BytesIO()
        image.save(output, format="PNG")
        filename = "detoure_" + os.path.splitext(os.path.basename(self.coffret_image.name))[0] + ".png"
        self.coffret_image.save(filename, ContentFile(output.getvalue()), save=False)
        self.__class__.objects.filter(pk=self.pk).update(coffret_image=self.coffret_image.name)


class Video(models.Model):
    title = models.CharField("titre", max_length=140)
    video = models.FileField("fichier vidéo", upload_to="videos/")
    is_published = models.BooleanField("publiée sur le site", default=True)
    created_at = models.DateTimeField("ajoutée le", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Vidéo"
        verbose_name_plural = "Vidéos"

    def __str__(self):
        return self.title
