from pathlib import Path
import os

# ============================
# 🔧 تحميل .env بشكل آمن
# ============================
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

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

CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if o.strip()
]

# ============================
# 📦 التطبيقات
# ============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "accounts",
    "catalog",
    "orders",
]

# ============================
# 👤 Custom User Model
# ============================
AUTH_USER_MODEL = "accounts.User"

# ============================
# ⚙️ Middleware
# ============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
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
# 🎨 Templates
# ============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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
# 🗄 Database
# ============================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ============================
# 🔐 Password validation
# ============================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ============================
# 🌍 Language & Time
# ============================
LANGUAGE_CODE = "ar-sa"
TIME_ZONE = "Asia/Riyadh"

USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ("ar", "العربية"),
    ("en", "English"),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

# ============================
# 📁 Static & Media Files (المهم هنا)
# ============================
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",   # ← ملفاتك أثناء التطوير
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # ← ناتج collectstatic

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ============================
# 🔑 Defaults
# ============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ============================
# 🔐 Auth redirects
# ============================
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# ============================
# 🧾 Logging
# ============================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

# ============================
# 🔒 Production Security
# ============================
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "same-origin"
    X_FRAME_OPTIONS = "DENY"
