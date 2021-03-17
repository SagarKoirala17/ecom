
from django.urls import path
from . import views
from .views import Login
urlpatterns=[
    path('login',Login.as_view(),name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
]