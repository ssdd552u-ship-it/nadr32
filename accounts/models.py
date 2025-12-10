from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    مستخدم مخصص لدعم التوسع لاحقًا
    - عميل
    - موظف / مدير
    """

    is_customer = models.BooleanField(default=True)
    is_staff_member = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Address(models.Model):
    """
    عناوين الشحن الخاصة بالعميل
    يتم نسخها داخل الطلب وقت الشراء
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.city}"
