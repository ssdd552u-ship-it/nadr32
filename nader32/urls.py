"""
URL configuration for nader32 project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة تحكم Django
    path("admin/", admin.site.urls),

    # تطبيق الحسابات (تسجيل – دخول – حسابي)
    path("accounts/", include("accounts.urls")),

    # المتجر (الصفحة الرئيسية – المنتجات – السلة)
    path("", include("catalog.urls")),

    # الطلبات (Checkout – الدفع – الطلبات)
    path("orders/", include("orders.urls")),
]

# ============================
# 📁 static & media (التطوير فقط)
# ============================
if settings.DEBUG:
    # ملفات الرفع (صور المنتجات…)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    # ❌ لا نضيف static هنا
    # Django يخدم static تلقائيًا من STATICFILES_DIRS أثناء التطوير
