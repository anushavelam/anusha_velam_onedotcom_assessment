# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:41:54 2025

Below code is to create a url patterns for ordering products

@author: Anusha
"""

from django.urls import path
from . import views
urlpatterns = [
        path('',views.product_list,name = 'product.list'),
        path('product/<int:id>/',
        views.product_detail,
        name = 'product_detail'),
        path('new/',views.product.product_create,
        name='product_create'),
        
        
        ]