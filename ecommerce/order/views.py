from django.shortcuts import render
from django.views import View
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User, auth
from django.views import View

from  product.models import Product
from .models import Order
from product.middleware.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):

    @method_decorator(auth_middleware)
    def get(self , request ):
        user = request.session.get('user_id')
        orders = Order.get_orders_by_customer(user)
        print(orders)
        return render(request , 'order/order.html', {'orders' : orders})

