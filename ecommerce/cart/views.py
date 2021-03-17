from django.shortcuts import render,redirect
from django.views import  View
from product.models import Product
from order.models import Order
from django.contrib.auth.models import User

# Create your views here.
class Cart(View):

    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(ids)
        print(products)
        context={
            'products':products
        }
        return render(request,'cart/cart.html',context)
class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone =request.POST.get('phone')
        user=request.session.get('user_id')
        cart=request.session.get('cart')
        products=Product.get_product_by_id(list(cart.keys()))

        for product in products:
            order=Order(user=User(id=user), product=product,phone=phone, address=address, price=product.price, quantity=cart.get(str(product.id)))
            print(order.placeOrder())
            request.session['cart']={}


        print(address,phone,user,cart,products)
        return redirect('cart')

    def get(self, request):
        return render(request,'cart/checkout.html')