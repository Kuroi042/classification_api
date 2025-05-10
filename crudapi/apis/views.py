from django.shortcuts import render

from rest_framework.response import Response
from . models import Product 
from . models import Users
from . serializers import ProductSerializer
from . serializers import UserSerializer

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
###############################################
###############################################
    
@api_view (['GET', 'POST'])
def intro(request):
    if request.method =='GET':
        users =  Users.objects.all() # get all the users
        serializer =  UserSerializer(users, many=True) # serilaize the users to be returned as json file
        return Response(serializer.data)       # return the serializers as jsonfile
    
    if request.method =='POST': #check for the method first
        serializer = UserSerializer(data = request.data) # get the new data 
        if serializer.is_valid(): # check if the data is valid
            serializer.save() #save it into db
            return Response(serializer.data) # return it as json


@api_view (['GET', 'PUT', 'DELETE'])
def getuserId(request , pk):

    try:
        user=Users.objects.get(id=pk)
   
    except  Users.DoesNotExist():
        return Response({'user is not found' }, status=404)
    
    if request.method =='GET':
        serializer =  UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer =  UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        user.delete()
        return Response({'user has been deleted succesfully'}, status=204)
    

        

            
        
            