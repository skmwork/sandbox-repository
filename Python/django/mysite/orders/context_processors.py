from .models import Order


def getting_basket_info(request):
    current_session_key = request.session.session_key
    if not current_session_key:
        request.session.cycle_key()

    try:
        order = Order.objects.get(session_key=current_session_key, is_basket=True)
        products_in_basket = order.productinorder_set.filter(is_active=True).order_by('-created')
    except Order.DoesNotExist:
        pass

    return(locals())