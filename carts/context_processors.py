from .models import CartItem, Cart
from .views import get_session_key

def cart_count(request):
  cart_items_count = 0
  current_user = request.user
  try:
    if current_user.is_authenticated:
      cart_items = CartItem.objects.filter(user=current_user)
    else:
      cart = Cart.objects.get(cart_id=get_session_key(request))
      cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
      cart_items_count += cart_item.quantity
  except Cart.DoesNotExist:
    pass

  return {'cart_count': cart_items_count}