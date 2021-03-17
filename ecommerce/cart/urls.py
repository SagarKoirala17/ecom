from django.urls import path,include
from . import views
from .views import Cart,Checkout
from product.middleware.auth import auth_middleware

urlpatterns = [
    path('', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out/' ,Checkout.as_view(),name='checkout')
]