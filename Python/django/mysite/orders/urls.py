from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path('add_product_to_basket', views.add_product_to_basket, name='add_product_to_basket'),
    path('delete_product_from_basket', views.delete_product_from_basket, name='delete_product_from_basket'),
    #delete_product_from_basket
]
