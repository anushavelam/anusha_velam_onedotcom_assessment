# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:42:47 2025

Below code is to add a product to order from customer view
@author: Anusha
"""
from django.views import views

def product_addition(request):
    print(request.POST)
    product_category = Category.Objects.all()
    if request.method == 'POST':
        
        label = request.POST['label'],
        description = request.POST['description'],
        quantity = request.POST['quantity'],
        
        data = Product(label = label, desciption = description , quantity = quantity)
        data.save()
    
        return HttpResponseRedirect('/products')
        
    return render(request, 'product/add.product.html')

def order(request):
    print(request.POST)
    if request.method == 'POST':
        
        price = request.POST['price']
        
        data = Pay(price = price)
        data.save()
        
        return HttpResponseRedirect('/thirdpartportal')
    
    


        
    
    
