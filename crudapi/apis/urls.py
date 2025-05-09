from django.urls import path 
from . import views

urlpatterns=[
    path('products', views.Product_list , name='products'),
]