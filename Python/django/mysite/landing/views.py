from django.shortcuts import render
from products.models import *


# Create your views here.
def home(request):
    products_images = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True)
    products_images_phones = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True, product__category__code='PHONE')
    products_images_laptops = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True, product__category__code='NTBK')
    return render(request, 'landing/home.html', locals())

