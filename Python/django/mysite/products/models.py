from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BoolanField(default=True)
    description = models.Text(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        erbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_active = models.BoolanField(default=True)
    image = models.ImageField(upload_to='/products_images/')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

