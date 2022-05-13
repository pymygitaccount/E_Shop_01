from django.contrib import admin

from store.models.customer import Customer
from store.models.orders import Order

from .models.category import Category
from .models.product import Product

# from .models.product import Product

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)


