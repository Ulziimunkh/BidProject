from django.urls import path
from . import views
app_name= 'BidCamp'
urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
]