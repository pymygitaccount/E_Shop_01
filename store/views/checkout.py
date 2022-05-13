# from django.shortcuts import render, redirect

# from django.contrib.auth.hashers import check_password
# from store.models.customer import Customer
# from django.views import View

# from store.models.product import Product
# from store.models.orders import Order


# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         products = Product.get_products_by_id(list(cart.keys()))
#         print(address, phone, customer, cart, products)


#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(customer = Customer(id = customer),
#             product = product,
#             price = product.price,
#             address = address,
#             phone = phone,
#             quantity = cart.get(str(product.id)))

    
#             order.save()
#         request.session['cart'] = {}

#         return redirect('cart')


#-------------------------------------------------------------------------
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from store.models.category import Category
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order

class CheckOut(View):        # class based view
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        customer = request.session.get('customer')
        
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer = Customer(id = customer),
            product = product,
            price = product.price,
            address = address,
            phone = phone,
            quantity = cart.get(str(product.id)))

            order.save()
            # print(order.placeOrder())
        request.session['cart'] = {}
        # request.session['cart'] = {}

        return redirect('cart') 
        

