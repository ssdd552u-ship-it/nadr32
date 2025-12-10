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

SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-secret-key-change-in-production')

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")


# ============================
# 📦 التطبيقات
# ============================

INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps (مشروع المتجر)
    'accounts',
    'catalog',
    'orders',
]


# ============================
# 👤 Custom User Model (مهم جدًا)
# ============================

AUTH_USER_MODEL = 'accounts.User'


# ============================
# ⚙️ Middleware
# ============================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================
# 🔗 URLs
# ============================

ROOT_URLCONF = 'nader32.urls'


# ============================
# 🎨 القوالب (Templates)
# ============================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================
# 🚀 WSGI
# ============================

WSGI_APPLICATION = 'nader32.wsgi.application'


# ============================
# 🗄 قاعدة البيانات
# ============================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================
# 🔐 التحقق من كلمات المرور
# ============================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


# ============================
# 🌍 اللغة والوقت
# ============================

LANGUAGE_CODE = 'ar-sa'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# ============================
# 📁 الملفات الثابتة والإعلامية
# ============================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


# ============================
# 📝 اللغات المتاحة
# ============================

LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]


# ============================
# 🔑 الإعدادات الافتراضية
# ============================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


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
