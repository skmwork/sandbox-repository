from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField('Позиция активна', default=True)
    code = models.CharField(max_length=5, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField('Позиция активна', default=True)
    discount = models.IntegerField('Скидка', default=0, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.price}, {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='products_images/')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField('Позиция активна', default=True)
    is_main = models.BooleanField('Позиция активна', default=False)

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'
