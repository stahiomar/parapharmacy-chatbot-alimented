from django.contrib import admin

from carts.models import *

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
  list_display = ['product', 'quantity', 'cart', 'user']

admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order_details)