from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Customer
# from ..webapp.models import Customer
# Create your views here.

def login(request):
    if request.method == 'POST':
        password= request.POST['password']
        username= request.POST['username']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect('login.html')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        phone_number= request.POST['phone_number']
        address= request.POST['address']
        identification= request.POST['identification']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        username= request.POST['username']

        if password1 == password2 :
            if Customer.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register.html')
            user = Customer.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            # customer = Customer.objects.create_user(phone_number=phone_number,identification=identification,address=address)
            user.save()
            # customer.save()
            messages.info(request, 'User Created')
            # messages.info(request, 'Customer Created')
            return redirect('login.html')
        else:
            print('password does not match')
            messages.info(request, 'Password does not match')
            return redirect('register.html')

        return redirect('login.html')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
