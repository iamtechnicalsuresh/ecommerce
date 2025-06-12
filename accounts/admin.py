from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CustomerProfile

# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number')}),
    )


@admin.register(CustomerProfile)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomerProfile
    list_display = ('user', 'full_name', 'phone', 'address')
    