from pathlib import Path
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from fanpage.models import SiteContent, TimelineMoment, FamilyMember, GalleryImage

IMG = Path(settings.BASE_DIR) / "fanpage" / "static" / "fanpage" / "img"


def attach(field, name):
    """Tayyor rasmni media/ papkasiga nusxalab, ImageField'ga biriktiradi."""
    with open(IMG / name, "rb") as f:
        field.save(name, File(f), save=False)


class Command(BaseCommand):
    help = "Sayt rasmlari, galereya, oila a'zolari va uchrashuv tarixini tayyor matn va rasm bilan to'ldiradi. Mavjud ma'lumotni o'chirmaydi."

    def handle(self, *args, **opts):
        # 1) Sayt rasmlari
        site = SiteContent.objects.first() or SiteContent(title="Riteish & Genelia")
        for field, name in (("hero_image", "hero.jpg"), ("story_image", "story.jpg"), ("family_image", "family.jpg")):
            if not getattr(site, field):
                attach(getattr(site, field), name)
        site.save()
        self.stdout.write("Sayt rasmlari tayyor")

        # 2) Galereya
        if not GalleryImage.objects.exists():
            for i, (title, name) in enumerate([
                ("Birinchi nigoh", "g1.jpg"), ("Ved", "g2.jpg"), ("Nikoh kuni", "g3.jpg"),
                ("Tujhe Meri Kasam", "g4.jpg"), ("Swarajya", "g5.jpg")], 1):
                g = GalleryImage(title=title, order=i)
                attach(g.image, name)
                g.save()
            self.stdout.write("Galereya to'ldirildi")

        # 3) Uchrashuv tarixi
        if not TimelineMoment.objects.exists():
            TimelineMoment.objects.bulk_create([
                TimelineMoment(year="2002", title="Birinchi uchrashuv", description="“Tujhe Meri Kasam” suratga olish maydonida tanishuv.", order=1),
                TimelineMoment(year="2003", title="Birinchi film", description="“Tujhe Meri Kasam” chiqdi — birgalikdagi kino yo‘li boshlandi.", order=2),
                TimelineMoment(year="2012", title="Nikoh", description="3-fevral kuni ikki yurak rasman bir bo‘ldi.", order=3),
                TimelineMoment(year="2014", title="Riaan", description="Oilada birinchi o‘g‘il dunyoga keldi.", order=4),
                TimelineMoment(year="2016", title="Rahyl", description="Ikkinchi o‘g‘il bilan oila to‘rt kishilik bo‘ldi.", order=5),
                TimelineMoment(year="2022", title="Ved", description="Riteish rejissyor, Genelia — bosh rolda: birgalikdagi yangi bob.", order=6),
            ])
            self.stdout.write("Uchrashuv tarixi to'ldirildi")

        # 4) Oila a'zolari (kattalarga rasm, bolalarning suratlarini o'zingiz yuklang)
        if not FamilyMember.objects.exists():
            for i, (name, role, photo) in enumerate([
                ("Riteish", "Ota", "g3.jpg"), ("Genelia", "Ona", "g1.jpg"),
                ("Riaan", "O‘g‘il", None), ("Rahyl", "O‘g‘il", None)], 1):
                m = FamilyMember(name=name, role=role, order=i)
                if photo:
                    attach(m.photo, photo)
                m.save()
            self.stdout.write("Oila a'zolari to'ldirildi")

        self.stdout.write(self.style.SUCCESS("Tayyor"))
