from pathlib import Path
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import models
from fanpage.models import SiteContent, Film, FamilyMember, GalleryImage
from fanpage.imaging import to_jpeg_bytes


class Command(BaseCommand):
    help = "Bazadagi hamma rasmni tiniq .jpg ga aylantiradi (jfif/avif/kichik rasmlar tuzatiladi)."

    def handle(self, *args, **opts):
        n = 0
        for Model in (SiteContent, Film, FamilyMember, GalleryImage):
            for obj in Model.objects.all():
                for f in obj._meta.fields:
                    if not isinstance(f, models.ImageField):
                        continue
                    ff = getattr(obj, f.name)
                    if not ff or ff.name.lower().endswith("_hd.jpg"):
                        continue
                    try:
                        with ff.storage.open(ff.name, "rb") as fh:
                            data = to_jpeg_bytes(fh)
                    except Exception as e:
                        self.stdout.write(f"O'tkazildi {ff.name}: {e}")
                        continue
                    ff.save(Path(ff.name).stem + "_hd.jpg", ContentFile(data), save=False)
                    obj.save()
                    n += 1
                    self.stdout.write(f"OK  {ff.name}")
        self.stdout.write(self.style.SUCCESS(f"{n} ta rasm tuzatildi"))
