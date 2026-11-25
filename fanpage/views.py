from django.shortcuts import render
from django.templatetags.static import static
from .models import SiteContent, Film, TimelineMoment, FamilyMember, GalleryImage

# Admin'da rasm yuklanmagan bo'lsa, shu tayyor rasmlar ko'rinadi (fanpage/static/fanpage/img/)
DEFAULT_GALLERY = [
    ("Birinchi nigoh", "fanpage/img/g1.jpg"),
    ("Ved", "fanpage/img/g2.jpg"),
    ("Nikoh kuni", "fanpage/img/g3.jpg"),
    ("Tujhe Meri Kasam", "fanpage/img/g4.jpg"),
    ("Swarajya", "fanpage/img/g5.jpg"),
]


def home(request):
    site = SiteContent.objects.first()

    def pick(field, default):
        f = getattr(site, field, None) if site else None
        return f.url if f else static(default)

    gallery = [{"title": g.title, "url": g.image.url} for g in GalleryImage.objects.all()]
    if not gallery:
        gallery = [{"title": t, "url": static(p)} for t, p in DEFAULT_GALLERY]

    context = {
        "site_content": site,
        "hero_url": pick("hero_image", "fanpage/img/hero.jpg"),
        "story_url": pick("story_image", "fanpage/img/story.jpg"),
        "family_url": pick("family_image", "fanpage/img/family.jpg"),
        "films": Film.objects.all(),
        "moments": TimelineMoment.objects.all(),
        "family_members": FamilyMember.objects.all(),
        "gallery": gallery,
    }
    return render(request, "fanpage/home.html", context)
