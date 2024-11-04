from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from carts.models import Order_details
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm
from store.models import Product

def get_session_key(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def cart(request):
    total = 0
    tax = 0
    full_total = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=get_session_key(request))
            cart_items = CartItem.objects.filter(cart=cart)

        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
        tax = 2 * total / 100
        full_total = total + tax
    except:
        cart = Cart.objects.create(cart_id=get_session_key(request))
        cart_items = CartItem.objects.filter(cart=cart)
        pass

    context = {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'full_total': full_total
    }
    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
    current_user = request.user
    if current_user.is_authenticated:
        product = Product.objects.get(id=product_id)
        try:
            cart_item = CartItem.objects.get(user=current_user, product=product)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(user=current_user, product=product, quantity=1)
        return redirect('cart')
    else:
        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=get_session_key(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=get_session_key(request))
        cart.save()
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=cart, product=product, quantity=1)
        return redirect('cart')

def decrement_from_cart(request, product_id, cart_id):
    product = Product.objects.get(id=product_id)
    current_user = request.user
    try:
        if current_user.is_authenticated:
            cart_item = CartItem.objects.get(user=current_user, product=product)
        else:
            cart = Cart.objects.get(cart_id=get_session_key(request))
            cart_item = CartItem.objects.get(cart=cart, product=product, id=cart_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

def remove_from_cart(request, product_id, cart_id):
    product = Product.objects.get(id=product_id)
    current_user = request.user
    try:
        if current_user.is_authenticated:
            cart_item = CartItem.objects.get(user=current_user, product=product)
        else:
            cart = Cart.objects.get(cart_id=get_session_key(request))
            cart_item = CartItem.objects.get(cart=cart, product=product, id=cart_id)
        cart_item.delete()
    except:
        pass
    return redirect('cart')

@login_required(login_url='login')
def checkout(request):
    current_user = request.user
    try:
        if current_user.is_authenticated:
            cart_items = CartItem.objects.filter(user=current_user)
        else:
            cart = Cart.objects.get(cart_id=get_session_key(request))
            cart_items = CartItem.objects.filter(cart=cart)
    except:
        if not current_user.is_authenticated:
            cart = Cart.objects.create(cart_id=get_session_key(request))
            cart_items = CartItem.objects.filter(cart=cart)
        pass

    context = {
        'cart_items': cart_items
    }
    return render(request, 'store/checkout.html', context)


def place_order(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        address_line_1 = request.POST['address_line_1']
        address_line_2 = request.POST.get('address_line_2', '')
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        order_note = request.POST.get('order_note', '')

        # Check for mandatory fields
        if not all([first_name, last_name, email, phone_number, address_line_1, city, state, country]):
            messages.warning(request, 'Please fill out all required fields.')
            return redirect('checkout')

        details = Order_details.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            country=country,
            order_note=order_note
        )
        details.save()

        messages.success(request, 'Order placed successfully!')
        return redirect('checkout')
    else:
        form = RegistrationForm()

    return render(request, 'store/checkout.html', {'form': form})
