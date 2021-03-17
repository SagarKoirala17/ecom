from django.urls import path,include
from . import views
from .views import OrderView
from product.middleware.auth import auth_middleware


urlpatterns = [
    path('', auth_middleware(OrderView.as_view()), name='order'),
]
