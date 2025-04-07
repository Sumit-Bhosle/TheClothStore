from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from ClothApp.models import Products
from accounts.models import Account
from django.contrib import messages
# Create your views here.

def add_to_cart(request, id):
    items = get_object_or_404(Products, id=id)

    # Get user ID or set it to None if not authenticated
    user_id = request.user.id if request.user.is_authenticated else None
    session_id = request.session.session_key

    # check if user has an active session
    if not session_id:
        request.session.save()
        session_id = request.session.session_key

    # get or create the cart item 
    cart_item, created = CartItem.objects.get_or_create(
        user_id = user_id,
        product = items
    )

    # for guest users, associate the cart_item with the session's cart
    if not user_id:
        cart, created_cart = Cart.objects.get_or_create(session_key=session_id)
        cart.items.add(cart_item)
    else:
        # for registered users, associate the cart_item with the users cart 

        user_instance = Account.objects.get(id=user_id)
        cart, created_cart = Cart.objects.get_or_create(user=user_instance, session_key=session_id)
        cart.items.add(cart_item)

        #handle quantity from the form
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity',1))

        if created: #if the cart item was just created
            cart_item.quantity = quantity
        else:
            # if the cart item already existed update the quantity
            cart_item.quantity += quantity
        
        cart_item.save()


    if not user_id:
        total_items_count = Cart.objects.get(session_key=session_id).items.count()
    else:
        total_items_count = sum(cart.items.all().count() for cart in request.user.cart.all())
    messages.success(request, f"{items.product_name} Added to cart Successfully")
    request.session["total_items_count"] = total_items_count
    return redirect("home")