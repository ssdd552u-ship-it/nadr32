from django.contrib import admin
from .models import User, Address


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_customer',
        'is_staff_member',
        'is_active',
    )
    list_filter = (
        'is_customer',
        'is_staff_member',
        'is_active',
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'user',
        'city',
        'phone',
        'created_at',
    )
    list_filter = ('city',)
    search_fields = ('full_name', 'phone', 'city')
