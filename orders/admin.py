from django.contrib import admin
from .models import Order, OrderItem, Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = (
        'product_name',
        'product_price',
        'quantity',
    )
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'status',
        'total_amount',
        'created_at',
    )
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__username')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'provider',
        'status',
        'amount',
        'created_at',
    )
    list_filter = ('status', 'provider')
    search_fields = ('order__id', 'transaction_id')
    readonly_fields = ('created_at',)
