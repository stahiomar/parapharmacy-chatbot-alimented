from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=500)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
