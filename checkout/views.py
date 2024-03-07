from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart,CartItem
from accounts.models import Account
from django.contrib import messages
from decimal import Decimal, ROUND_HALF_UP
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse
from .models import Order,OrderItem


# Create your views here.
def checkout_page(request):

    user_id = request.user.id if request.user.is_authenticated else None
    session_id = request.session.session_key

    if not user_id:
        cart,created_cart = Cart.objects.get_or_create(session_key=session_id)
    else:
        user_instance = get_object_or_404(Account,id=user_id)
        cart,created_cart = Cart.objects.get_or_create(user=user_instance,session_key=session_id)


    # for handling quantity updates and removal
    if request.method=="POST":
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity',1))

        cart_item = get_object_or_404(CartItem,id=cart_item_id)

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart.items.remove(cart_item)
            cart_item.delete()

    cart.refresh_from_db()

    total_price = Decimal('0.0')
    for cart_item in cart.items.all():
        item_price = Decimal(cart_item.product.product_price)
        item_quantity = Decimal(cart_item.quantity)
        item_total_price = (item_price*item_quantity).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
        total_price += item_total_price
        cart_item.total_price = item_total_price

    #rounding the total price upto 2 decimal
    total_price = total_price.quantize(Decimal('0.0'),rounding=ROUND_HALF_UP)

    #for GST clac
    tax_percentage = Decimal('0.18')
    tax = (tax_percentage*total_price).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

    #calc grand total including GST
    grand_total = (total_price+tax).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

    context = {
        'cart_items':cart.items.all(),
        'total_price':total_price,
        'tax':tax,
        'grand_total':grand_total
    }

    return render(request,"place-order.html",context)

#to change to + , - , changes in price,total,tax in cart(checkout)
@csrf_exempt
def update_quantity(request):
    if request.method == "POST" and request.headers.get('x-requested-with')=='XMLHttpRequest':
        cart_item_id = request.POST.get('cart_item_id')
        quantity_change = int(request.POST.get('quantity_change'))
        cart_item_data = get_object_or_404(CartItem,id=cart_item_id)
        cart_item_data.quantity += quantity_change
        cart_item_data.save()

        total_price = calculate_total_price(cart_item_data)
        tax = calculate_tax(total_price)
        grand_total = (total_price+tax).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

    #return data to frontend
        # response_data= {
        #     'cart_item_id':cart_item_id,
        #     'item_total_price':cart_item_data.cost_per_item,
        #     'total_price':total_price,
        #     'tax':tax,
        #     'grand_total':grand_total
        # }
        response_data = {
            'success':True,
        }
        return JsonResponse(response_data)   #ajax return with help of jsonResponse

    else:
        return JsonResponse({'error':'Bad Request'})
    
def calculate_total_price(cart_item_data):
    item_price = Decimal(cart_item_data.product.product_price)
    item_quantity = Decimal(cart_item_data.quantity)
    total_price = (item_price*item_quantity).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
    return total_price

def calculate_tax(total_price):
    tax_percentage = Decimal('0.18')
    tax = (tax_percentage*total_price).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
    return tax


@csrf_exempt
def remove_item(request,cart_item_id):
    if request.method=="POST" and request.headers.get('x-requested-with')=='XMLHttpRequest':
        cart_item_data = get_object_or_404(CartItem,id=cart_item_id)
        cart_item_data.delete()
        response_data = {
            'success':True,
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error':'Bad Request'})
    
def final_order(request):
    user_id = request.user.id if request.user.is_authenticated else None
    session_id = request.session.session_key

    if not user_id:
        cart,_ = Cart.objects.get_or_create(user=user_instance,session_key=session_id)

    else:
        user_instance = get_object_or_404(Account,id=user_id)
        cart,_ = Cart.objects.get_or_create(session_key=session_id)


        total_price = Decimal('0.0')
        for cart_item in cart.items.all():
            item_price = Decimal(cart_item.product.product_price)
            item_quantity = Decimal(cart_item.quantity)
            item_total_price = (item_price*item_quantity).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
            total_price += item_total_price
            cart_item.total_price = item_total_price
            
        #rounding the total price upto 2 decimal
        total_price = total_price.quantize(Decimal('0.0'),rounding=ROUND_HALF_UP)

        #for GST clac
        tax_percentage = Decimal('0.18')
        tax = (tax_percentage*total_price).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

        #calc grand total including GST
        grand_total = (total_price+tax).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)

        context = {
            'cart_items':cart.items.all(),
            'total_price':total_price,
            'tax':tax,
            'grand_total':grand_total
        }

        return render(request,"final_order.html",context)
                
@csrf_exempt
def update_create_order(request):
    if request.method == "POST":
        payment_id = request.POST.get('payment_id')
        total_price = request.POST.get('total_price')
        tax = request.POST.get('tax')
        grand_total = request.POST.get('grand_total')
        user_email = request.POST.get('user_email')

        try:
            user = Account.objects.get(email=user_email)
            cart_items = CartItem.objects.filter(user=user)
        except Account.DoesNotExist:
            return JsonResponse({'error':'User Not Found'},status=400)
        
        order,created = Order.objects.get_or_create(payment_id=payment_id, defaults={
            'total_price':total_price,
            'tax':tax,
            'grand_total':grand_total,
            'user':user,
            'status':'Pending'
        })

        # updating the Order Status
        order.status = "Processing"
        order.save()
        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity
            order_item,created = OrderItem.objects.get_or_create(order=order,product=product,defaults={'quantity':quantity})

            #if item is already available update the quantity
            if not created:
                order_item.quantity += quantity

            order_item.save()

        return JsonResponse({'message':'Order Created Successfully'})
    
    return JsonResponse({'message':'Invalid User Request'})
    


def thank_you_page(request):
    return render(request, "thank_you_page.html")

