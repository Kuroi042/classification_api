from django.shortcuts import render

from rest_framework.response import Response
from . models import Product 
from . models import Users
from . serializers import ProductSerializer
from . serializers import registrationSerializer

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
    except Product.DoesNotExist: 
        var  = 'product not fouznd'
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
# Productserializer convert the product Object to Jsonfile format 
    if request.method == 'GET':
        serializer =  ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        #we added product cuz we ill update the product 
        serializer =  ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        product.delete()
        return Response({'user has been deleted'},status=204)
###############################################
###############################################




@api_view(['POST'])
def register(request):
    if request.method =='POST':
        serializer = registrationSerializer(data =  request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()
            name  = user.username
            print(name)
            data['response'] = 'Succesfully ' +name +' created '
        else :
            data = serializer.errors   
        return Response(data)     

            
        
            