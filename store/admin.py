from django.contrib import admin

from store.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug', 'stock', 'is_available', 'category', 'date_modified'] # pour afficher les champs précisé dans le panneau admin
    prepopulated_fields = {"slug": ["product_name"]} # pour convertir le champ category_name en slug. Ex : category_name = T Shirts ===> slug = t-shirts


admin.site.register(Product, ProductAdmin)
