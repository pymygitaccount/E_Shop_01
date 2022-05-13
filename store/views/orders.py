
import imp
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from store.models.category import Category
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.orders import *
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):        # class based view

    
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders' : orders})
    