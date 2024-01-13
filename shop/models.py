from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/', blank=True)
    desc = models.CharField(max_length=30,)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    rating = models.FloatField()
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) 
    

