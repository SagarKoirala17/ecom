from django.urls import path,include
from . import views
from .views import Index


urlpatterns = [
    path('', Index.as_view(), name='product'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/product_description',views.product_description,name='product_description'),



]
