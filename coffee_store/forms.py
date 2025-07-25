from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Category, Menu

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture', 'address']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'image', 'category', 'description', 'price', 'availability', 'available_servings']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
