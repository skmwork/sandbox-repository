from django.shortcuts import render
from products.models import *


# Create your views here.
def product(request, product_id):


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    product = Product.objects.get(id=product_id)
    return render(request, 'products/product.html', locals())
