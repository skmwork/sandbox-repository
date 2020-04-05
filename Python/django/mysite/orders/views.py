from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import *
from products.models import *
import decimal


def basket_list(order):
    basket_products = order.productinorder_set.filter(is_active=True).order_by('-created')
    result = dict()
    result['total_price'] = order.total_price
    result['products'] = []
    for p in basket_products:
        prd = dict()
        prd['name'] = p.product.name
        prd['price'] = p.product.price
        prd['nmb'] = p.nmb
        prd['id'] = p.id
        result['products'].append(prd)
    return result


def add_product_to_basket(request):
    current_session_key = request.session.session_key
    if not current_session_key:
        request.session.cycle_key()
    data = request.POST
    product_id = data.get('product_id')
    print(product_id)

    nmb = decimal.Decimal(data.get('nmb'))
    print(product_id, nmb)
    product = Product.objects.get(id=product_id)
    try:
        order = Order.objects.get(session_key=current_session_key, is_basket=True)
    except Order.DoesNotExist:
        order = Order(session_key=current_session_key, is_basket=True)
        order.save()
    product_in_order, created = order.productinorder_set.get_or_create(product_id=product.id,
                                                                       order_id=order.id,
                                                                       session_key=current_session_key,
                                                                       defaults={"nmb": nmb},
                                                                       )
    if not created and product_in_order.is_active == True:
        product_in_order.nmb += nmb
        product_in_order.save()

    if not created and product_in_order.is_active == False:
        product_in_order.nmb = nmb
        product_in_order.is_active = True
        product_in_order.save()

    return JsonResponse({'basket_products': basket_list(order)})


def delete_product_from_basket(request):
    current_session_key = request.session.session_key
    if not current_session_key:
        request.session.cycle_key()
    data = request.POST
    product_in_basket_id = data.get('product_in_basket_id')
    product_in_basket = ProductInOrder.objects.get(id=product_in_basket_id, session_key=current_session_key)
    product_in_basket.is_active = False
    product_in_basket.save()
    order = Order.objects.get(session_key=current_session_key, is_basket=True, id=product_in_basket.order_id)
    return JsonResponse({'basket_products': basket_list(order)})





