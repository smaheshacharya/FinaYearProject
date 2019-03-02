from django.shortcuts import render
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request,'index.html')


def register(request):
    return render(request,'register.html')

def shop_grid(request):
    return render(request,'shop-grid.htm')
