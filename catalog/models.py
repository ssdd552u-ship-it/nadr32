from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="اسم التصنيف"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="المعرف (Slug)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="التصنيف"
    )

    name = models.CharField(
        max_length=255,
        verbose_name="اسم المنتج"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="المعرف (Slug)"
    )
    description = models.TextField(
        blank=True,
        verbose_name="وصف المنتج"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="الكمية المتوفرة"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="متاح للبيع"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="المنتج"
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name="صورة المنتج"
    )

    class Meta:
        verbose_name = "صورة منتج"
        verbose_name_plural = "صور المنتجات"

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name="المستخدم"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "سلة"
        verbose_name_plural = "السلال"

    def __str__(self):
        return f"سلة - {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="السلة"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )

    class Meta:
        verbose_name = "عنصر في السلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
