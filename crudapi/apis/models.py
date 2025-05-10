from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name  = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    




class Users(models.Model):
    fname =models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    nickname= models.CharField(max_length=10)
    age = models.IntegerField(3)
    
    def __str__(self):
        return self.nickname
    
