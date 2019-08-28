from django.shortcuts import render
from .models import DVD
# Create your views here.

def home(request):

    dvd1 = DVD()
    dvd1.name = 'John Wick the second coming'
    dvd1.desc = 'A movie where Keanu Reeves Dog dies, and he kills everyone in the movie'
    dvd1.inStock = True

    dvd2 = DVD()
    dvd2.name = 'Shawshank Redmption'
    dvd2.desc = 'A movie about rape in prison'
    dvd2.inStock = True

    dvd3 = DVD()
    dvd3.name = 'Lion King 2'
    dvd3.desc = 'A movie about Lions coming of age'
    dvd3.inStock = False

    dvd4 = DVD()
    dvd4.name = 'Dave Chapelle'
    dvd4.desc = 'A movie about Lions coming of age'
    dvd4.inStock = False
    
    dvds = [dvd1,dvd2,dvd3, dvd4]
    return render(request, 'home.html', {'dvds':dvds})