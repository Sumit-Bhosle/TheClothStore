from django.contrib import admin
from .models import Category,Products
from django.utils.html import format_html
from accounts.models import Account


class CustomProducts(admin.ModelAdmin):
    list_display = ['product_name','product_price','gender','product_description','img_display'] 
    list_per_page = 5
    list_filter = ['gender','product_price']
    search_fields = ['product_name']


    #  Method To display Images in Admin Panel using format_html
    def img_display(self,obj):
        return format_html ('<img src = "{}" width="90" height= "100" />',obj.product_image.url)
    

# Register your models here.

admin.site.register(Category)
admin.site.register(Products,CustomProducts)

admin.site.register(Account)
# CUSTOMIZATONS - 
admin.site.site_header="Cloth Store Application" # Change admin panel Header 
admin.site.index_title="ClothStore Admin"        # Change admin panel title

