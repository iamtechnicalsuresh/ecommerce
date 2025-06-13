from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5  # Max 5 image upload fields

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['title', 'seller', 'price', 'stock', 'created_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)