from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from product.models import Product

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(first_name=first_name,last_name=last_name, password=password, email=email,
                                                    username=username)
                    user.save()
                    messages.success(request, "You are now registered")
                    return redirect('login')





        else:
            messages.error(request, "Passwords didnot match")
            return redirect('register')



    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['user_id']=user.id
            request.session['username'] = user.username
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('index')
        else:
            messages.error(request, "Wrong username and password")
            return redirect('login')



    else:
        return render(request, 'account/login.html')
def logout(request):
    if request.method=="POST":
      auth.logout(request)
      messages.success(request,"You are logged out")
      return redirect('index')

