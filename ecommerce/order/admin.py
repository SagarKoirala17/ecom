from django.contrib import admin
from .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','price','address'),
    list_per_page = 25,
    list_display_links = ('user','product')

admin.site.register(Order)