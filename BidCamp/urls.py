from django.urls import path
from . import views
app_name= 'BidCamp'
urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
    path('product/', views.product, name='product'),
    path('product2/', views.product2, name='product2'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('icons/', views.icons, name='icons'),
    path('payment/', views.payment, name='payment'),
    path('single2/', views.single2, name='single2'),
    path('terms/', views.terms, name='terms'),
    path('typography/', views.typography, name='typography'),

]