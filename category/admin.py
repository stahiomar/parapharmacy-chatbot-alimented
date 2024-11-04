from django.contrib import admin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', 'description'] # pour afficher les champs précisé dans le panneau admin
    prepopulated_fields = {"slug": ["category_name"]} # pour convertir le champ category_name en slug. Ex : category_name = T Shirts ===> slug = t-shirts


# Register your models here.
# pour afficher le(s) model(s) dans le panneau admin
admin.site.register(Category, CategoryAdmin)