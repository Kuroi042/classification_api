from django.urls import path 
from . import views

urlpatterns=[
    path('products', views.Product_list , name='products'),
path('product/<int:pk>/' , views.product , name='product'),
    path('intro/' , views.intro),
    path('getuser/<int:pk>/',views.getuserId),
]