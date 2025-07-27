from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user():
        pass
        # extra_fields.get_by_natural_key(username)
        # extra_fields.setdefault('is_admin', False)
        # return self.create_user(username, password, **extra_fields)
    

    def create_superuser(self, username, password=None, **extra_fields):
        # user = self.create_user(username, first_name, last_name, email, phone, password)
        # self.is_staff = is_staff
        # self.is_superuser = is_superuser

        # user.is_staff = True
        # user.is_superuser = True
        # user.save(using=self._db)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', default='media/profile_pictures/image.png')
    address = models.CharField(max_length=200)
    date_created = models.DateField()
    date_updated = models.DateField()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']

    objects = CustomUserManager()
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Menu(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/menu_images/', blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    availability = models.BooleanField()
    availble_servings = models.IntegerField()

class Cart(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    total_amount = models.FloatField()

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    menu = models.OneToOneField('Menu', on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    sub_total = models.FloatField()
    date_created = models.DateField()
    date_updated = models.DateField()

class UserOrder(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    total_amount = models.FloatField()
    billing_address = models.CharField(max_length=200)

class UserOrderItem(models.Model):
    user_order = models.ForeignKey('UserOrder', on_delete=models.CASCADE)
    menu = models.OneToOneField('Menu', on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    sub_total = models.FloatField()
    date_created = models.DateField()
    date_updated = models.DateField()