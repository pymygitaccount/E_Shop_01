from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_qty')
def cart_qty(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * cart_qty(product , cart)


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)

    return sum
    

    
#-----------------------------------------------------


# from unittest import TestProgram

# from django import template

# register = template.Library()

# # filter function created to get the products in cart
# @register.filter(name='is_in_cart')                # decorator
# def is_in_cart(product, cart):
#     keys = cart.keys()
#     for id in keys:
#         if int(id) == product.id:
#             return True
#     return False


# # filter function is created to get the Qty of products in cart
# @register.filter(name='cart_qty')
# def cart_qty(product, cart):
#     keys = cart.keys()
#     for id in keys:
#         if int(id) == product.id:
#             return cart.get(id)
#     return 0
    

# @register.filter(name='price_total')
# def price_total(product, cart):
#     return product.price * cart_qty(product, cart)


# @register.filter(name='total_cart_price')
# def total_cart_price(products, cart):
#     sum = 0
#     for p in products:
#         sum += price_total(p, cart)
#     return sum
  

 