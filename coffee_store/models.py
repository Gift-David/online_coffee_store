from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='', default='')
    address = models.CharField(max_length=200)
    date_created = models.DateField()
    date_updated = models.DateField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email', 'phone']

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Menu(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    availability = models.BooleanField()
    availble_servings = models.IntegerField()

class Cart(models.Model):
    user = models.OneToOneField()
    total_amount = models.FloatField()

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    menu = models.OneToOneField('Menu', on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    sub_total = models.FloatField()
    date_created = models.DateField()
    date_updated = models.DateField()

class UserOrder(models.Model):
    user = models.OneToOneField()
    total_amount = models.FloatField()
    billing_address = models.CharField(max_length=200)

class UserOrderItem(models.Model):
    user_order = models.ForeignKey('UserOrder', on_delete=models.CASCADE)
    menu = models.OneToOneField('Menu', on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    sub_total = models.FloatField()
    date_created = models.DateField()
    date_updated = models.DateField()