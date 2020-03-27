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
    customer_email = models.EmailField(max_length=48, balnk=True, default=None)
    status = models.ForeignKey(Status, blank=True, Null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Пользователь {self.customer_name} {self.customer_email} Заказ №{self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, Null=True, default=None)
    product = models.ForeignKey(Product, blank=True, Null=True, default=None)

