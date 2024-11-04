from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Cart(models.Model):
  cart_id = models.CharField(max_length=255)
  date_add = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.cart_id


class CartItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  quantity = models.IntegerField()
  def __str__(self):
    return self.product.product_name

  def total_product_price(self):
    return self.product.price * self.quantity
  
class Order_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    order_note = models.TextField(blank=True, null=True)
    def __str__(self):
      return f"{self.first_name} {self.last_name}"