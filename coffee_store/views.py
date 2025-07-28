from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MenuForm

# Create your views here.

def menu_list(request):
    return HttpResponse('Menu list')

def add_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('')
        else:
            form = MenuForm()
    return render()
    pass


