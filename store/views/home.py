from itertools import product
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from store.models.category import Category
from store.models.customer import Customer
from store.models.product import Product
from django.views import View
# Create your views here.

import logging

logger = logging.getLogger("eshop_log")

class Index(View):
    def post(self, request):
        product = request.POST.get('product') 
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart 
        print('cart :- ', request.session['cart'])

        return redirect('homepage')
        

    def get(self, request):
        cart = request.session.get("cart")
        if not cart:
            request.session.cart = {}    # creating empty cart
            
        products = None
        categories = Category.get_all_category()
        categoryID = request.GET.get('category')
        
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID )
            logger.info("Get all products by catagory Id.")
            
        else:
            products = Product.get_all_product()

        data = {}
        data['products'] = products
        data['categories'] = categories

        print('You are:-', request.session.get('email'))

        return render(request, 'index.html', data)











