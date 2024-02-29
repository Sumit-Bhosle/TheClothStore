from django.db import models
from ClothApp.models import Products
from accounts.models import Account
# Create your models here.

#cart detail with product information
class CartItem(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def cost_per_item(self):
        return self.quantity * self.product.product_price     #price show on cart page

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"
                                   
class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.email if self.user else 'Guest'}"

