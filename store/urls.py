from unicodedata import name

from django.urls import path

from .views import Index, home, login, signup
from .views.cart import Cart
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.checkout import CheckOut
from .views.orders import Order, OrderView
from store.middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name= 'homepage'),
    path('logout', logout, name='logout'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='order'),


] 
