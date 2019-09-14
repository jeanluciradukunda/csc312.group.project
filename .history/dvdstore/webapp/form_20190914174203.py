from django import forms
from .models import DVD, Customer
from django.contrib.auth.models import User, auth
from django.db import models

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ('Title','year','genre','PriceDVD','InStock','Synopsis','BookingPickup' ,'NumOfTimesRented','ImageDVD')
        widgets = { 'Synopsis': forms.TextInput(attrs={'size': 50})}


class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        #user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)

        fields = ('username','password','email','first_name','last_name','phone_number','address','identification')

class customerForm2:
    class Meta:
        model= Customer
        fields = ('username','password','email','first_name','last_name','phone_number','address','identification','isStaff')

