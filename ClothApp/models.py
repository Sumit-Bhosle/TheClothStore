from django.db import models

# Create your models here.

class  Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
class Products(models.Model):
    gender_option = (('men','MEN'),('women','WOMEN'),('unisex','UNISEX'))
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="Prod_Images",default=None)
    image_file = models.CharField(max_length=255, default="default.jpg")
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,choices=gender_option)

    def __str__(self):
        return self.product_name    # Used to auto set names to each product inserted into table.

    class meta: 
        db_table = "Product"
