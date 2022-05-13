from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

import logging

logger = logging.getLogger("eshop_log")

class Cart(View):
    def get(self , request):
        logger.info("Entering into the Cart...!")
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        logger.info("Get the product by ID...!!")
        print(products)
        return render(request , 'cart.html' , {'products' : products} )


#--------------------------------------------------------------
# from django.contrib.auth.hashers import check_password, make_password
# from django.shortcuts import redirect, render
# from django.views import View
# from store.models.category import Category
# from store.models.customer import Customer
# from store.models.product import Product


# class Cart(View):
#     def get(self , request):
#         ids = list(request.session.get('cart').keys())
#         products = Product.get_products_by_id(ids)
#         print(products)
#         return render(request , 'cart.html' , {'products' : products} )

   