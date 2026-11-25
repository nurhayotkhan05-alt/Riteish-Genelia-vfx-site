from pathlib import Path
import mimetypes

# .jfif/.avif/.webp ni brauzer rasm sifatida taniydi (Windows'da ba'zan yo'q bo'ladi)
for _ext, _mt in ((".jfif","image/jpeg"),(".avif","image/avif"),(".webp","image/webp")):
    mimetypes.add_type(_mt, _ext)
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-change-this-before-deployment"
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ["django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles", "fanpage"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware", "django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "uz"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR/"fanpage"/"static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR/"media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
