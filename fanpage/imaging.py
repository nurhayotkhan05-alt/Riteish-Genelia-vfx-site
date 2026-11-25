"""Yuklangan rasmlarni brauzer hamma joyda ko'rsata oladigan, chiroyli JPEG'ga aylantiradi."""
import io
from pathlib import Path
from django.core.files.base import ContentFile
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

TARGET_W = 1800   # kichik rasmlar shu kenglikkacha kattalashtiriladi
MAX_SIDE = 2600


def enhance(img):
    img = ImageOps.exif_transpose(img).convert("RGB")
    w, h = img.size
    if w < TARGET_W:
        k = min(TARGET_W / w, 3.5, MAX_SIDE / max(w, h))
        if k > 1:
            img = img.filter(ImageFilter.MedianFilter(3)) if w < 700 else img  # JPEG shovqinini yumshatadi
            img = img.resize((round(w * k), round(h * k)), Image.LANCZOS)
            img = img.filter(ImageFilter.UnsharpMask(radius=2.0, percent=85, threshold=2))
    elif max(w, h) > MAX_SIDE:
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.05)
    img = ImageEnhance.Color(img).enhance(1.07)
    return img


def to_jpeg_bytes(fileobj):
    fileobj.seek(0)
    img = Image.open(fileobj)
    buf = io.BytesIO()
    enhance(img).save(buf, "JPEG", quality=90, optimize=True, progressive=True)
    return buf.getvalue()


def normalize_fieldfile(ff):
    """Yangi yuklangan faylni .jpg qilib saqlaydi (ff.save chaqiradi, instance.save() qilmaydi)."""
    stem = Path(ff.name).stem
    data = to_jpeg_bytes(ff.file)
    ff.save(stem + ".jpg", ContentFile(data), save=False)
