from django.contrib import admin
from .models import CustomUser, Category, Menu, UserOrder, UserOrderItem

# Register your models here.

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['']

# class CustomAdmin(admin.ModelAdmin):
#     fields = ['Menu', 'Category']

admin.site.register([CustomUser, Category, Menu, UserOrder, UserOrderItem])
