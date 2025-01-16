# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:42:17 2025

Below code to store additional details and authentication for shopowner
Using boolean function to check if the user is Shopowner
@author: Anusha
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

class CustomUser(Abstractor):
    is_shop_owner = models.BooleanField(default=False)
    
class ShopOwner(models.Model):
    user = models.OneTooneField(CustomerUser,on_delete = models.CASCADE)
    shopname = models.OneTooneField(Shop,on_delete = models.CASCADE)
    
class Category(models.Model):
    product_type = model.CharField(max_length = 50)
    
    def __str__(self):
        return self.product_type
    
class product(models.Model):
    label = model.CharField(max_length = 50)
    description = model.CharField(max_length = 150)
    quantity = model.IntegerField()
    price = model.IntegerField()
    
    def __str__(self):
        return self.label
    
    
    


    
    

    
    

