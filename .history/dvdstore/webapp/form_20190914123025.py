from django import forms
from .models import DVD, Customer

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ('Title','year','genre','InStock','Synopsis','BookingPickup' ,'NumOfTimesRented','ImageDVD')


class customerForm:
    class Meta:
        model= Customer
        fields = ('phone_number','address','genre','InStock','Synopsis','BookingPickup' ,'NumOfTimesRented','ImageDVD')

