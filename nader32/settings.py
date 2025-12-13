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
    h.strip() for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if h.strip()
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
# ✅ تعريف مسار القوالب العام (C:\Users\hp\nader32\templates)
TEMPLATES_DIR = BASE_DIR / "templates"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # ✅ هنا التعريف الأساسي لمجلد templates
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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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

# ============================
# 📝 اللغات المتاحة + مسار ملفات الترجمة (اختياري لكنه ممتاز)
# ============================
LANGUAGES = [
    ("ar", "العربية"),
    ("en", "English"),
]

# إذا بتسوي ترجمة مخصصة لاحقًا (django.po)
LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# ============================
# 📁 الملفات الثابتة والإعلامية
# ============================
STATIC_URL = "static/"

# ✅ مهم: تأكد أن المجلد موجود فعلاً: C:\Users\hp\nader32\static
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# (اختياري للإنتاج) مكان تجميع static عند deploy
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# ============================
# 🔑 الإعدادات الافتراضية
# ============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ============================
# 🧱 إعدادات جلسات ورسائل (اختياري)
# ============================
# لو تبغى مسار تسجيل الدخول/الخروج
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# ============================
# 🔒 أمان إضافي للإنتاج
# ============================
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # إعدادات كويسة للـ headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "same-origin"
