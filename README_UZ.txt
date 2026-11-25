RITEISH & GENELIA — DJANGO LOYIHASI

1) Papkani oching, terminalda shu papkaga kiring.
2) Virtual muhit: py -m venv venv
3) Aktivlashtirish (Windows PowerShell): .\venv\Scripts\Activate.ps1
4) Kutubxonalar: pip install -r requirements.txt
5) Migratsiya: py manage.py makemigrations fanpage
6) Bazani yaratish: py manage.py migrate
7) Admin foydalanuvchi: py manage.py createsuperuser
8) Server: py manage.py runserver
9) Sayt: http://127.0.0.1:8000/
10) Admin: http://127.0.0.1:8000/admin/

ADMINDA NIMALARNI TO‘LDIRASIZ?
- Sayt rasmlari: SiteContent qo‘shib, hero_image, story_image, family_image yuklang. Bitta SiteContent yozuvi yetarli.
- Filmlar: poster va tavsiflarni Film bo‘limida qo‘shing.
- Uchrashuv tarixi: TimelineMoment bo‘limida qo‘shing.
- Oila a’zolari: FamilyMember bo‘limida qo‘shing.
- Galereya: GalleryImage bo‘limida rasmlarni yuklang.

Rasmlar media/ papkasiga saqlanadi. ImageField ishlashi uchun Pillow o‘rnatiladi.
Hozircha SQLite ishlatiladi. Saytning asosiy dizayni berilgan HTML fayldan olindi.

---- YANGILANISHLAR ----
- Sayt to'liq animatsiyali: harflar ko'tarilishi, oltin tovlanish, zarrachalar, Ken Burns (rasm sekin yaqinlashishi),
  3D kartalar, chiziq chizilishi, sanagichlar, suzuvchi yuraklar, galereya lightbox.
- Rasmlar endi saytingiz ichidan (internetdagi havolalarsiz) olinadi: fanpage/static/fanpage/img/
  Admin'da rasm yuklasangiz, o'sha ko'rinadi; yuklamasangiz — tayyor rasmlar turadi.
- Bo'sh jadvallarni to'ldirish (ixtiyoriy): py manage.py seed_demo

---- RASMLAR HAQIDA ----
- Admin'dan yuklangan har qanday rasm (jfif, avif, png...) avtomatik tiniq .jpg ga aylanadi va kattalashtiriladi.
- Eski rasmlarni ham tuzatish: py manage.py fix_images
- Oila a'zolarining rasmlari endi saytda ko'rinadi (Oila a'zolari bo'limidan yuklang).
