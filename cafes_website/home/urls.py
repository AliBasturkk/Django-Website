from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hakkimizda/', views.about, name='about'),
    path('hizmetlerimiz/', views.services, name='services'),
    path('iletisim/', views.contact, name='contact'),
    path('sirket-politikamiz/', views.company_policy, name='company_policy'),
]
