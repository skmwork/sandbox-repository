from django.db import models
from products.models import *
from django.db.models.signals import post_save


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Статус {self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    customer_name = models.CharField(max_length=128, null=True, blank=True, default=None)
    customer_email = models.EmailField(max_length=48, null=True, blank=True, default=None)
    status = models.ForeignKey(Status, blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comment = models.TextField('Комментарий', null=True, blank=True, default=None)
    total_price = models.DecimalField('Общая стоимость', default=0, max_digits=10, decimal_places=2)
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_basket = models.BooleanField('В корзине', default=False)

    def __str__(self):
        return f'Пользователь {self.customer_name} {self.customer_email} Заказ №{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField('Количество товаров', null=True, blank=True, default=1)
    price_per_item = models.DecimalField('Цена за единицу', default=0, max_digits=10, decimal_places=2)
    total_price = models.DecimalField('Суммарная стоимость', default=0, max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField('Активная позиция', default=True)
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.product.name} - {self.nmb} по цене {self.price_per_item}'

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        nmb = self.nmb
        print(price_per_item, nmb)

        self.price_per_item = price_per_item
        self.total_price = nmb*price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price+=item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)



