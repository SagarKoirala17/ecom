from django.shortcuts import render, redirect
from product.models import Product,Category

from django.contrib import messages


# Create your views here.

def index(request):

        product = Product.objects.order_by('-upload_date')[:4]



        context = {
            'product': product,



        }

        return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
