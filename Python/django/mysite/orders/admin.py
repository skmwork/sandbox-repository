from django.contrib import admin

from .models import Status, Order, ProductInOrder


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInline]


admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder)
