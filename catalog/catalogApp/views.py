from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . import models

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def sistemas(request):
    return render(request, 'home/sistemas.html')