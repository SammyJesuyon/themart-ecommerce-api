from turtle import title
from django.db import models
from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Store(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Product(models.Model):
    title = models.CharField(max_length=500)
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    condition = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class ProductImage(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

class Cart(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    return "%s/%s.%s" % ("img", datetime.now(), ext)

class FileUpload(models.Model):
    img = models.ImageField(upload_to=upload_location)