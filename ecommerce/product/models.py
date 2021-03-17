from django.core.exceptions import ValidationError
from django.db import models

from datetime import datetime


def minpricevalidator(value):
    if value > 0:
        return True
    else:
        raise ValidationError("Price must be greator than 0")


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    price = models.FloatField(validators=[minpricevalidator])
    size = models.CharField(max_length=3, blank=True)
    color = models.CharField(max_length=100, blank=True)
    upload_date = models.DateTimeField(default=datetime.now)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return  Product.objects.order_by('-upload_date')
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

