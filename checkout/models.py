from django.db import models
from ClothApp.models import Products
from accounts.models import Account
import uuid

# Create your models here.
class OrderItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ord = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items', default = 'None')
    
    def __str__(self) :
        return f"{self.quantity} x {self.product.product_name}"
    

class Order(models.Model):
    ORDER_STATUS_CHOICES  = [
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
    ]

    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    order_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    payment_id = models.CharField(max_length=200)
    items = models.ManyToManyField(OrderItem)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    tax = models.DecimalField(max_digits=10,decimal_places=2)
    grand_total = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=ORDER_STATUS_CHOICES,default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
