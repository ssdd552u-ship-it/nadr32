from pathlib import Path
import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# ============================
# 📁 المسار الأساسي
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================
# 🔐 الأمان (Security)
# ============================
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key-change-in-production")

DEBUG = os.getenv("DEBUG", "True").strip().lower() == "true"

ALLOWED_HOSTS = [
    h.strip()
    for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if h.strip()
]

# (اختياري) لو عندك دومين/https ضيفه في .env مثل:
# CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com
CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]

# ============================
# 📦 التطبيقات
# ============================
INSTALLED_APPS = [
    # Django Core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Apps (مشروع المتجر)
    "accounts",
    "catalog",
    "orders",
]

# ============================
# 👤 Custom User Model (مهم جدًا)
# ============================
AUTH_USER_MODEL = "accounts.User"

# ============================
# ⚙️ Middleware
# ============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    # مهم للغة العربية
    "django.middleware.locale.LocaleMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ============================
# 🔗 URLs
# ============================
ROOT_URLCONF = "nader32.urls"

# ============================
# 🎨 القوالب (Templates)
# ============================
TEMPLATES_DIR = BASE_DIR / "templates"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ============================
# 🚀 WSGI / ASGI
# ============================
WSGI_APPLICATION = "nader32.wsgi.application"
ASGI_APPLICATION = "nader32.asgi.application"

# ============================
# 🗄 قاعدة البيانات
# ============================
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", str(BASE_DIR / "db.sqlite3")),
    }
}

# ============================
# 🔐 التحقق من كلمات المرور
# ============================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ============================
# 🌍 اللغة والوقت
# ============================
LANGUAGE_CODE = "ar-sa"
TIME_ZONE = "Asia/Riyadh"

USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ("ar", "العربية"),
    ("en", "English"),
]

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# ============================
# 📁 الملفات الثابتة والإعلامية
# ============================
# ✅ لازم تبدأ بشرطة / عشان الروابط تطلع صحيحة
STATIC_URL = "/static/"

# ✅ تأكد أن المجلد موجود فعلاً: <project_root>/static
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# ✅ للإنتاج (collectstatic)
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ لازم تبدأ بشرطة /
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ============================
# 🔑 الإعدادات الافتراضية
# ============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ============================
# 🧱 إعدادات جلسات ورسائل (اختياري)
# ============================
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# ============================
# 🧾 Logging (يساعدك جدًا بالتتبع)
# ============================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("LOG_LEVEL", "INFO"),
    },
}

# ============================
# 🔒 أمان إضافي للإنتاج
# ============================
if not DEBUG:
    # كوكيز آمنة
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # إعادة توجيه HTTPS
    SECURE_SSL_REDIRECT = True

    # لو شغال خلف Proxy/Nginx (يمنع loop)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # HSTS
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "31536000"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "same-origin"
    X_FRAME_OPTIONS = "DENY"
