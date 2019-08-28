from django.shortcuts import render
from .models import DVD
# Create your views here.

def home(request):

    dvds = DVD.objects.all() #imports dvds from database

    return render(request, 'home.html', {'dvds':dvds})