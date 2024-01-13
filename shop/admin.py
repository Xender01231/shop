from django.contrib import admin
from .models import Product
from .models import Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','image','desc','price','discount','rating','stock','is_available',)
    #list_editable = ('image','desc','price','discount','rating','stock','is_available',)
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','product','delivery_address','created_at',)    