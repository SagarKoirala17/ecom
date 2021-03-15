from django.shortcuts import render, get_object_or_404, redirect

from .models import Category
from .models import Product
from django.views import View

# Create your views here.
class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        cart= request.session.get('cart')
        if cart:
            quantity=cart.get('product')
            if quantity:
                 cart[product]= quantity + 1
            else:
                cart[product]=1

        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('product')




    def get(self,request):
        product = None
        cart=request.session.get('cart')
        if  not cart:
            request.session.cart={}


        category = Category.get_all_categories()
        categoryId = request.GET.get('category')

        if categoryId:
            print(categoryId)
            product = Product.get_all_product_by_category_id(categoryId)
        else:
            product = Product.objects.order_by('-upload_date')
        context = {
            'product': product,
            'category': category,

        }

        return render(request, 'product/product.html', context)



def product_description(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    context={
        'product':product,
    }
    return render(request,'product/productDetail.html',context)



def search(request):
    queryset_list=Product.objects.order_by('-upload_date')

    if 'products' in request.GET:
        products=request.GET['products']
        if products:
            queryset_list=queryset_list.filter(name__icontains=products)


    context={
        'product': queryset_list,
        'values': request.GET,


    }
    return render(request,'product/search.html',context)
