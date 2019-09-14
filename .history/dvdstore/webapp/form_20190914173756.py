from django import forms
from .models import DVD, Customer
from django.contrib.auth.models import User, auth
from django.db import models

class DocumentForm(forms.ModelForm):
    long_desc = forms.CharField(widget=forms.Textarea(attrs={'cols': 5, 'rows': 2}))
    short_desc = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = DVD.CharField(widget=forms.Textarea(attrs={'cols': 5, 'rows': 2}))
        fields = ('Title','year','genre','PriceDVD','InStock','Synopsis','BookingPickup' ,'NumOfTimesRented','ImageDVD')


class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        #user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)

        fields = ('username','password','email','first_name','last_name','phone_number','address','identification')

class customerForm2:
    class Meta:
        model= Customer
        fields = ('username','password','email','first_name','last_name','phone_number','address','identification','isStaff')

