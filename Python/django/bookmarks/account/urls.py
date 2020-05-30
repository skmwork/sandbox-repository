from django.conf.urls import include, url
from django.contrib.auth import login, logout#, logout_then_login
from . import views


urlpatterns = [
    url('dashboard', views.dashboard, name='dashboard'),
    url('register', views.register, name='register'),
    url('edit/', views.edit, name='edit'),
]
