from django.db import models
from products.models import Product


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
    customer_name = models.CharField(max_length=128)
    customer_email = models.EmailField(max_length=48, blank=True, default=None)
    status = models.ForeignKey(Status, blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comment = models.TextField('Комментарий', null=True, blank=True, default=None)
    total_price = models.DecimalField('Общая стоимость', default=0, max_digits=10, decimal_places=2)

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

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'

