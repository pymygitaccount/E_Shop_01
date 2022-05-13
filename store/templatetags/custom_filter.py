from unittest import TestProgram

from django import template

register = template.Library()

# filter function created for currency conversion
@register.filter(name='currency')                # decorator
def currency(number):
    return "₹" + str(number)


@register.filter(name='multiply')                # decorator
def multiply(number, number1):
    return number * number1



