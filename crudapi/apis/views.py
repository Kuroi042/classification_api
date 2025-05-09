from django.shortcuts import render

from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET' , 'POST'])
def Product_list(request):
    if request.method == 'GET':
        #fetch all databases
        products = Product.objects.all()
        #many=True for serializing all products
        serializer =  ProductSerializer(products ,many=True)
        #return json file serializer
        return Response(serializer.data)
    
    if request.method =='POST':
        # get the data from the request
        serializer = ProductSerializer(data =request.data) 
        #check if the data is valid
        if serializer.is_valid():
            #save the product in the db
            serializer.save()
            #return the new created product 
            return Response(serializer.data)


@api_view(['GET' , 'PUT' , 'DELETE'])
def product(request, pk): # request referes to GET put delete
    try:
        #primarry key 
        product =Product.objects.get(id=pk) #find the product using id
    except Product.DoesNotExist(): 
        return Response(status=404)
# Productserializer convert the product Object to Jsonfile format 
    if request.method == 'GET':
        serializer =  ProductSerializer(product)
        return Response(serializer.data)