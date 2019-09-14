from django import forms
from .models import DVD

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ('Title','year','genre','InStock','Synopsis','BookingPickup' ,'NumOfTimesRented','ImageDVD')


class customerForm:
    class Meta:
        model

