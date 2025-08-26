from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('aylik-menu/', views.monthly_menu, name='monthly_menu'),
]