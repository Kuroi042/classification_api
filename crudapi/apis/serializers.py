from rest_framework import serializers
from . models import  Product
from . models import Users


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['id', 'name' , 'description' , 'price' ]
         

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =Users
        fields=['id', 'fname', 'lname','age','nickname']