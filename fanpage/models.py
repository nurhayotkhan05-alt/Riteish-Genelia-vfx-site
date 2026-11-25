from django.db import models
from .imaging import normalize_fieldfile


class ImageNormalizeMixin(models.Model):
    """Admin'dan yuklangan har qanday rasm (jfif, avif, png...) avtomatik tiniq .jpg ga aylanadi."""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        for f in self._meta.fields:
            if isinstance(f, models.ImageField):
                ff = getattr(self, f.name)
                if ff and not ff._committed:
                    try:
                        normalize_fieldfile(ff)
                    except Exception:
                        pass  # rasm o'qilmasa, asl holicha saqlanadi
        super().save(*args, **kwargs)

class SiteContent(ImageNormalizeMixin):
    """Bosh sahifa, hikoya va oila bo‘limlari uchun asosiy rasmlar."""
    title = models.CharField(max_length=150, default="Riteish & Genelia")
    hero_image = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="Bosh sahifa rasmi")
    story_image = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="Uchrashuv rasmi")
    family_image = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="Oilaviy rasm")
    class Meta:
        verbose_name = "Sayt rasmlari"
        verbose_name_plural = "Sayt rasmlari"
    def __str__(self): return self.title

class Film(ImageNormalizeMixin):
    title = models.CharField(max_length=150, verbose_name="Film nomi")
    year = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Yili")
    genre = models.CharField(max_length=100, blank=True, verbose_name="Janri")
    tagline = models.CharField(max_length=180, blank=True, verbose_name="Qisqa yozuv")
    description = models.TextField(blank=True, verbose_name="Film haqida")
    poster = models.ImageField(upload_to="films/posters/", blank=True, null=True, verbose_name="Poster rasmi")
    art_text = models.CharField(max_length=30, blank=True, verbose_name="Poster ustidagi belgi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Film"
        verbose_name_plural = "Filmlar"
    def __str__(self): return self.title

class TimelineMoment(models.Model):
    year = models.CharField(max_length=30, verbose_name="Yil")
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    description = models.CharField(max_length=250, verbose_name="Tavsif")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    class Meta:
        ordering = ["order", "year"]
        verbose_name = "Tarixiy lahza"
        verbose_name_plural = "Uchrashuv tarixi"
    def __str__(self): return f"{self.year} — {self.title}"

class FamilyMember(ImageNormalizeMixin):
    name = models.CharField(max_length=100, verbose_name="Ismi")
    role = models.CharField(max_length=100, blank=True, verbose_name="Oiladagi o‘rni")
    photo = models.ImageField(upload_to="family/", blank=True, null=True, verbose_name="Rasmi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Oila a’zosi"
        verbose_name_plural = "Oila a’zolari"
    def __str__(self): return self.name

class GalleryImage(ImageNormalizeMixin):
    title = models.CharField(max_length=120, verbose_name="Rasm nomi")
    image = models.ImageField(upload_to="gallery/", verbose_name="Rasm")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Galereya rasmi"
        verbose_name_plural = "Galereya rasmlari"
    def __str__(self): return self.title
