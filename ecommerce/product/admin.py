from django.contrib import admin
from .models import Product
from .models import Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price','size','upload_date','category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'upload_date', 'price')
    list_per_page = 25

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)