from django.contrib import admin

from .models import Product, ProductImage, ProductCategory


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)

