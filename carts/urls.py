from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<product_id>', views.add_to_cart, name='add_to_cart'),
    path('decrement_from_cart/<product_id>/<cart_id>', views.decrement_from_cart, name='decrement_from_cart'),
    path('remove_from_cart/<product_id>/<cart_id>', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),  # Use a different path for the checkout view
    path('place_order', views.place_order, name='place_order')  # Use a different path for the place_order view
]
