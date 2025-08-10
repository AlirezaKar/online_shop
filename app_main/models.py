from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'customer',
        SALESPERSON = 'sales person'

    phone_number = models.CharField(max_length=11, unique=True, null=True, blank=True)
    role = models.CharField(max_length=12, choices=Role.choices, default=Role.CUSTOMER)
    product_count = models.PositiveIntegerField(max_length=2, default=0)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        REJECTED = 'rejected'
        APPROVED = 'approved'

    name = models.CharField(max_length=50, null=True) 
    price = models.IntegerField(default=0)   
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='Uncategorized')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    rating = models.IntegerField(null=True)  

    def __str__(self):
        return self.name

class ProductFeature(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)
    field_name = models.CharField(max_length=50, null=True)
    field_content = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"feature N.{self.id}"


class Comment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        REJECTED = 'rejected'
        APPROVED = 'approved'

    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    content = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    text = models.TextField(null=True)

    def __str__(self):
        return f"{self.user.username}::{self.text[:8:1]}"
    
class MultiMedia(models.Model):
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    content = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='files', null=True)
    file = models.FileField(upload_to='./product', null=True)
    
    def __str__(self):
        return f"{self.id} :: {self.content.name}"
    
