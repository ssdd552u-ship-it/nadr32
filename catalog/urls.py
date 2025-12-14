from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    # الصفحة الرئيسية
    path("", views.home, name="home"),
]
