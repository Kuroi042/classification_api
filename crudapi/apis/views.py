from django.shortcuts import render

from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET' , 'POST'])
def Product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer =  ProductSerializer(products ,many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer = ProductSerializer(data =request.data) # get the data from the request
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        