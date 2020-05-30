from django.urls import path

from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.index, name='index'),
    path('product/<int:product_id>', views.product, name='product'),
]
