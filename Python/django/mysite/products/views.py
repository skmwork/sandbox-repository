from django.shortcuts import render
from .models import *


# Create your views here.
def product(request, product_id):


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())


def index(request):
    products_images = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True)
    products_images_phones = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True, product__category__code='PHONE')
    products_images_laptops = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True, product__category__code='NTBK')
    return render(request, 'products/index.html', locals())
